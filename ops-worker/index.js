/**
 * Flying M Ops Board — Cloudflare Worker API
 *
 * Routes:
 *   GET    /cards         → return all cards as JSON array
 *   POST   /cards         → create a card (body: JSON card object)
 *   PATCH  /cards/:id     → update fields on a card (body: partial card)
 *   DELETE /cards/:id     → delete a card
 *
 * KV binding: OPS_BOARD  (key = card ID, value = JSON string)
 * All cards also stored under key "ALL_IDS" as a JSON array of IDs for listing.
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

async function getAllIds(kv) {
  const raw = await kv.get('ALL_IDS');
  return raw ? JSON.parse(raw) : [];
}

async function setAllIds(kv, ids) {
  await kv.put('ALL_IDS', JSON.stringify(ids));
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
      const ids = await getAllIds(kv);
      const cards = [];
      for (const id of ids) {
        const raw = await kv.get(id);
        if (raw) cards.push(JSON.parse(raw));
      }
      // Sort by created date ascending
      cards.sort((a, b) => new Date(a.created || 0) - new Date(b.created || 0));
      return json(cards);
    }

    // POST /cards
    if (method === 'POST' && path === '/cards') {
      let card;
      try { card = await request.json(); } catch { return err('Invalid JSON'); }
      if (!card.id || !card.title || !card.column) return err('Missing required fields: id, title, column');

      // Validate column
      const validCols = ['Backlog', 'In Progress', 'Done'];
      if (!validCols.includes(card.column)) return err('Invalid column');

      await kv.put(card.id, JSON.stringify(card));
      const ids = await getAllIds(kv);
      if (!ids.includes(card.id)) {
        ids.push(card.id);
        await setAllIds(kv, ids);
      }
      return json(card, 201);
    }

    // PATCH /cards/:id
    const patchMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (method === 'PATCH' && patchMatch) {
      const id = patchMatch[1];
      const existing = await kv.get(id);
      if (!existing) return err('Card not found', 404);

      let updates;
      try { updates = await request.json(); } catch { return err('Invalid JSON'); }

      const card = { ...JSON.parse(existing), ...updates, id }; // id is immutable
      await kv.put(id, JSON.stringify(card));
      return json(card);
    }

    // DELETE /cards/:id
    const deleteMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (method === 'DELETE' && deleteMatch) {
      const id = deleteMatch[1];
      await kv.delete(id);
      const ids = await getAllIds(kv);
      await setAllIds(kv, ids.filter(i => i !== id));
      return json({ deleted: id });
    }

    return err('Not found', 404);
  }
};
