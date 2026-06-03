/**
 * Flying M Ops Board — Cloudflare Worker + Durable Object API
 *
 * Uses a Durable Object (single writer, strongly consistent) instead of KV.
 * Routes:
 *   GET    /cards         → return all cards as JSON array
 *   POST   /cards         → create a card
 *   PATCH  /cards/:id     → update fields on a card
 *   DELETE /cards/:id     → delete a card
 */

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Cache-Control': 'no-store',
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

// ── Durable Object ────────────────────────────────────────────────────────────
export class OpsBoard {
  constructor(state) {
    this.state = state;
  }

  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method.toUpperCase();

    const validCols = ['Preflight', 'Enroute', 'Landed', 'Flying M'];

    // GET /cards
    if (method === 'GET' && path === '/cards') {
      const cards = (await this.state.storage.get('cards')) || [];
      cards.sort((a, b) => new Date(a.created || 0) - new Date(b.created || 0));
      return json(cards);
    }

    // POST /cards
    if (method === 'POST' && path === '/cards') {
      let card;
      try { card = await request.json(); } catch { return err('Invalid JSON'); }
      if (!card.id || !card.title || !card.column) return err('Missing required fields');
      if (!validCols.includes(card.column)) return err('Invalid column');

      const cards = (await this.state.storage.get('cards')) || [];
      if (cards.find(c => c.id === card.id)) return err('Duplicate card ID', 409);
      cards.push(card);
      await this.state.storage.put('cards', cards);
      return json(card, 201);
    }

    // PATCH /cards/:id
    const patchMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (method === 'PATCH' && patchMatch) {
      const id = patchMatch[1];
      const cards = (await this.state.storage.get('cards')) || [];
      const idx = cards.findIndex(c => c.id === id);
      if (idx === -1) return err('Card not found', 404);
      let updates;
      try { updates = await request.json(); } catch { return err('Invalid JSON'); }
      cards[idx] = { ...cards[idx], ...updates, id };
      await this.state.storage.put('cards', cards);
      return json(cards[idx]);
    }

    // DELETE /cards/:id
    const deleteMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (method === 'DELETE' && deleteMatch) {
      const id = deleteMatch[1];
      const cards = (await this.state.storage.get('cards')) || [];
      const filtered = cards.filter(c => c.id !== id);
      await this.state.storage.put('cards', filtered);
      return json({ deleted: id });
    }

    return err('Not found', 404);
  }
}

// ── Worker entrypoint ─────────────────────────────────────────────────────────
export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS });
    }

    // Route all requests to the single Durable Object instance
    const id = env.OPS_BOARD_DO.idFromName('main');
    const stub = env.OPS_BOARD_DO.get(id);

    // Forward request to DO, then add CORS headers to response
    const resp = await stub.fetch(request);
    const body = await resp.text();
    return new Response(body, {
      status: resp.status,
      headers: { 'Content-Type': 'application/json', ...CORS },
    });
  }
};
