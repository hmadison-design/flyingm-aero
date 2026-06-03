/**
 * Flying M Ops Board — Cloudflare Worker API
 *
 * Routes:
 *   GET    /cards         → return all cards as JSON array
 *   POST   /cards         → create a card (body: JSON card object)
 *   PATCH  /cards/:id     → update fields on a card (body: partial card)
 *   DELETE /cards/:id     → delete a card
 *
 * KV binding: OPS_BOARD
 * All cards stored under a single key "CARDS" as a JSON array.
 * This avoids eventual-consistency issues with multiple KV keys.
 */

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS },
  });
}

function err(msg, status = 400) {
  return json({ error: msg }, status);
}

async function getCards(kv) {
  const raw = await kv.get('CARDS');
  return raw ? JSON.parse(raw) : [];
}

async function putCards(kv, cards) {
  await kv.put('CARDS', JSON.stringify(cards));
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method.toUpperCase();
    const kv = env.OPS_BOARD;

    // CORS preflight
    if (method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS });
    }

    // GET /cards
    if (method === 'GET' && path === '/cards') {
      const cards = await getCards(kv);
      cards.sort((a, b) => new Date(a.created || 0) - new Date(b.created || 0));
      return json(cards);
    }

    // POST /cards
    if (method === 'POST' && path === '/cards') {
      let card;
      try { card = await request.json(); } catch { return err('Invalid JSON'); }
      if (!card.id || !card.title || !card.column) return err('Missing required fields: id, title, column');

      const validCols = ['Preflight', 'Enroute', 'Landed', 'Flying M'];
      if (!validCols.includes(card.column)) return err('Invalid column');

      const cards = await getCards(kv);
      if (cards.find(c => c.id === card.id)) return err('Duplicate card ID', 409);
      cards.push(card);
      await putCards(kv, cards);
      return json(card, 201);
    }

    // PATCH /cards/:id
    const patchMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (method === 'PATCH' && patchMatch) {
      const id = patchMatch[1];
      const cards = await getCards(kv);
      const idx = cards.findIndex(c => c.id === id);
      if (idx === -1) return err('Card not found', 404);

      let updates;
      try { updates = await request.json(); } catch { return err('Invalid JSON'); }

      cards[idx] = { ...cards[idx], ...updates, id }; // id is immutable
      await putCards(kv, cards);
      return json(cards[idx]);
    }

    // DELETE /cards/:id
    const deleteMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (method === 'DELETE' && deleteMatch) {
      const id = deleteMatch[1];
      const cards = await getCards(kv);
      const filtered = cards.filter(c => c.id !== id);
      await putCards(kv, filtered);
      return json({ deleted: id });
    }

    return err('Not found', 404);
  }
};
