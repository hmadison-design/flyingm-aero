
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

changes = []

# ── 1. Hero: seniority line + LinkedIn ────────────────────────────────────────
old = '      <p class="hero-descriptor">\n        Building the systems that teach pilots how to fly, stay sharp, and come home safe.\n      </p>'
new = '      <p class="hero-title-line">Director, Instructional Design &amp; Content &nbsp;&middot;&nbsp; Redbird Flight Simulations &nbsp;&middot;&nbsp; <a href="https://www.linkedin.com/in/harveyemadison/" target="_blank" rel="noopener">LinkedIn &#8599;</a></p>\n      <p class="hero-descriptor">\n        Building the systems that teach pilots how to fly, stay sharp, and come home safe.\n      </p>'
assert old in html, 'FAIL 1'
html = html.replace(old, new, 1)
changes.append('1. Hero seniority + LinkedIn')

# ── 2. GIFT origin story ───────────────────────────────────────────────────────
old = '        <div class="project-subtitle">Guided Independent Flight Training — Private Pilot</div>\n        <div class="project-stat-line">33 modules · One cohesive system · A decade in active use</div>'
new = '        <div class="project-subtitle">Guided Independent Flight Training — Private Pilot</div>\n        <div class="project-origin">Built where four previous attempts failed — including a team that helped build Microsoft Flight Simulator. GIFT shipped 18 months after Harvey joined Redbird. It remains the only product of its kind.</div>\n        <div class="project-stat-line">33 modules · One cohesive system · A decade in active use</div>'
assert old in html, 'FAIL 2'
html = html.replace(old, new, 1)
changes.append('2. GIFT origin story')

# ── 3. Shorey outcomes + quote ─────────────────────────────────────────────────
old = '        <p class="project-impact-line">Thousands of copies sold. Hundreds of pilots trained. There\'s a reasonable chance the pilot who flew you home last Thanksgiving learned to fly using GIFT.</p>'
new = '''        <p class="project-impact-line">Thousands of copies sold. Hundreds of pilots trained. There's a reasonable chance the pilot who flew you home last Thanksgiving learned to fly using GIFT.</p>

        <div class="project-outcomes">
          <div class="outcome-stat-row">
            <span class="outcome-stat">43 hrs</span>
            <span class="outcome-label">Average time to private pilot certificate at Skyline Aviation — well below the national average of 67 hours</span>
          </div>
          <div class="outcome-stat-row">
            <span class="outcome-stat">$134–161</span>
            <span class="outcome-label">Per-hour student savings using Redbird AATD vs. training airplane</span>
          </div>
        </div>

        <blockquote class="project-quote">
          <p>"The proof that using GIFT as heavily as we do works can be seen in our time-to-certificate numbers. On average our private pilot students pass their checkrides with only 43 hours in their logbooks. That only happens because of GIFT in our Redbird simulators."</p>
          <cite>— Jonathan Shorey, CEO, Skyline Aviation &nbsp;(Part 61 &amp; Part 141 · Angelo State University)</cite>
        </blockquote>'''
assert old in html, 'FAIL 3'
html = html.replace(old, new, 1)
changes.append('3. Shorey outcomes + quote')

# ── 4. Independent projects: reframe intro ─────────────────────────────────────
old = '''        <p class="ind-intro">
          The work Harvey does outside of Redbird isn't a side hustle — it's the
          same mission running on a different track. When you believe something
          strongly enough, you build toward it on your own time too. These projects
          exist because the GA community needed them, and waiting for someone else
          to build them wasn't an option.
        </p>'''
new = '''        <p class="ind-intro">
          This is what passion combined with genuine effectiveness looks like. These projects
          don't compete with Harvey's career — they extend it. Each one exists because the
          GA community needed it and no one else was building it. That's not being scattered.
          That's what happens when conviction meets capability and neither one backs down.
        </p>'''
assert old in html, 'FAIL 4'
html = html.replace(old, new, 1)
changes.append('4. Independent projects reframed')

# ── 5. About: add telecom leadership credential ────────────────────────────────
old = '''            <span class="cred-text">Webster Trophy — Flight Scenario Challenge Designer &amp; volunteer Board member</span>
          </div>
        </div>'''
new = '''            <span class="cred-text">Webster Trophy — Flight Scenario Challenge Designer &amp; volunteer Board member</span>
          </div>
          <div class="cred-row reveal reveal-delay-3">
            <div class="cred-icon">
              <svg viewBox="0 0 12 12"><circle cx="6" cy="6" r="4"/></svg>
            </div>
            <span class="cred-text">Former senior leader, Fortune 500 telecommunications — team of 70+ highly technical staff</span>
          </div>
        </div>'''
assert old in html, 'FAIL 5'
html = html.replace(old, new, 1)
changes.append('5. Telecom leadership added')

# ── 6. Copyright: dynamic year ─────────────────────────────────────────────────
old = '© 2025 Harvey Madison — All rights reserved'
new = '© <span id="copy-year"></span> Harvey Madison — All rights reserved'
assert old in html, 'FAIL 6'
html = html.replace(old, new, 1)
old_script = "window.addEventListener('DOMContentLoaded', function() {"
new_script = "window.addEventListener('DOMContentLoaded', function() {\n  var yr = document.getElementById('copy-year');\n  if (yr) yr.textContent = new Date().getFullYear();"
assert old_script in html, 'FAIL 6b'
html = html.replace(old_script, new_script, 1)
changes.append('6. Dynamic copyright year')

# ── 7. CSS for new elements ────────────────────────────────────────────────────
old_css = '.btn {\n  font-family: var(--font-display);\n  font-weight: 700;'
new_css = '''.hero-title-line {
  font-family: var(--font-display);
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--sky);
  margin-bottom: 16px;
  opacity: 0.9;
}
.hero-title-line a { color: var(--sky); opacity: 0.7; transition: opacity 0.2s; }
.hero-title-line a:hover { opacity: 1; }

.project-origin {
  font-family: var(--font-body);
  font-size: 0.82rem;
  font-style: italic;
  color: var(--amber);
  line-height: 1.55;
  margin-bottom: 14px;
  opacity: 0.88;
  padding-left: 12px;
  border-left: 2px solid rgba(232,160,48,0.5);
}

.project-outcomes {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.outcome-stat-row {
  display: flex;
  align-items: baseline;
  gap: 12px;
}
.outcome-stat {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 1.5rem;
  color: var(--amber);
  white-space: nowrap;
  flex-shrink: 0;
  line-height: 1.2;
}
.outcome-label {
  font-family: var(--font-body);
  font-size: 0.84rem;
  color: var(--mist);
  line-height: 1.45;
  opacity: 0.8;
}

.project-quote {
  margin-top: 20px;
  padding: 16px 18px;
  border-left: 3px solid rgba(46,143,168,0.45);
  background: rgba(46,143,168,0.06);
}
.project-quote p {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 0.92rem;
  color: var(--mist);
  line-height: 1.65;
  margin: 0 0 10px 0;
}
.project-quote cite {
  font-family: var(--font-display);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sky);
  font-style: normal;
  opacity: 0.75;
}

.btn {
  font-family: var(--font-display);
  font-weight: 700;'''
assert old_css in html, 'FAIL 7'
html = html.replace(old_css, new_css, 1)
changes.append('7. New CSS added')

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)

print('SUCCESS. All changes applied:')
for c in changes:
    print(' ', c)
print('File length:', len(html))
