/**
 * Flying M Ops Board — Cloudflare Worker + Durable Object + R2
 *
 * Card routes (via Durable Object — strongly consistent):
 *   GET    /cards             → all cards
 *   POST   /cards             → create card
 *   PATCH  /cards/:id         → update card fields
 *   DELETE /cards/:id         → delete card
 *
 * File routes (via R2):
 *   POST   /upload            → upload a file, returns {url, name, size}
 *   DELETE /files/:filename   → delete a file from R2
 */

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, X-Filename, X-Filesize',
  'Cache-Control': 'no-store',
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS },
  });
}
function err(msg, status = 400) { return json({ error: msg }, status); }

// ── Durable Object ────────────────────────────────────────────────────────────
export class OpsBoard {
  constructor(state) { this.state = state; }

  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method.toUpperCase();
    const validCols = ['Preflight', 'Enroute', 'Landed', 'Flying M'];

    if (method === 'GET' && path === '/cards') {
      const cards = (await this.state.storage.get('cards')) || [];
      cards.sort((a, b) => new Date(a.created || 0) - new Date(b.created || 0));
      return json(cards);
    }

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

    const idMatch = path.match(/^\/cards\/([a-zA-Z0-9_-]+)$/);
    if (idMatch) {
      const id = idMatch[1];
      const cards = (await this.state.storage.get('cards')) || [];

      if (method === 'PATCH') {
        const idx = cards.findIndex(c => c.id === id);
        if (idx === -1) return err('Card not found', 404);
        let updates;
        try { updates = await request.json(); } catch { return err('Invalid JSON'); }
        if (updates.column && !validCols.includes(updates.column)) return err('Invalid column');
        cards[idx] = { ...cards[idx], ...updates, id };
        await this.state.storage.put('cards', cards);
        return json(cards[idx]);
      }

      if (method === 'DELETE') {
        const filtered = cards.filter(c => c.id !== id);
        await this.state.storage.put('cards', filtered);
        return json({ deleted: id });
      }
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

    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method.toUpperCase();

    // ── R2 upload ──────────────────────────────────────────────────────────
    if (method === 'POST' && path === '/upload') {
      try {
        const filename = request.headers.get('X-Filename') || `file-${Date.now()}`;
        const safe = filename.replace(/[^a-zA-Z0-9._-]/g, '_');
        const key = `${Date.now()}-${safe}`;
        const body = await request.arrayBuffer();
        await env.OPS_FILES.put(key, body, {
          httpMetadata: { contentType: request.headers.get('Content-Type') || 'application/octet-stream' },
        });
        const fileUrl = `https://ops-board-files.${url.hostname.split('.').slice(-2).join('.')}/files/${key}`;
        // Use a stable public URL pattern
        const publicUrl = `https://ops-board-api.hmadison.workers.dev/files/${key}`;
        return json({ url: publicUrl, name: filename, key, size: body.byteLength }, 201);
      } catch (e) {
        return err('Upload failed: ' + e.message, 500);
      }
    }

    // ── R2 file serve ──────────────────────────────────────────────────────
    if (method === 'GET' && path.startsWith('/files/')) {
      const key = path.slice('/files/'.length);
      const obj = await env.OPS_FILES.get(key);
      if (!obj) return new Response('Not found', { status: 404 });
      return new Response(obj.body, {
        headers: {
          'Content-Type': obj.httpMetadata?.contentType || 'application/octet-stream',
          'Cache-Control': 'public, max-age=31536000',
          ...CORS,
        },
      });
    }

    // ── R2 file delete ─────────────────────────────────────────────────────
    if (method === 'DELETE' && path.startsWith('/files/')) {
      const key = path.slice('/files/'.length);
      await env.OPS_FILES.delete(key);
      return json({ deleted: key });
    }

    // ── Card routes → Durable Object ───────────────────────────────────────
    const id = env.OPS_BOARD_DO.idFromName('main');
    const stub = env.OPS_BOARD_DO.get(id);
    const resp = await stub.fetch(request);
    const body = await resp.text();
    return new Response(body, {
      status: resp.status,
      headers: { 'Content-Type': 'application/json', ...CORS },
    });
  }
};
