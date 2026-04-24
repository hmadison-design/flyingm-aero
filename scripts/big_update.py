
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# ── 1. HERO: add seniority credential line below name ──────────────────────────
old_descriptor = '''      <p class="hero-descriptor">
        Building the systems that teach pilots how to fly, stay sharp, and come home safe.
      </p>'''
new_descriptor = '''      <p class="hero-title-line">Director of Instructional Design &amp; Content &nbsp;·&nbsp; Redbird Flight Simulations</p>
      <p class="hero-descriptor">
        Building the systems that teach pilots how to fly, stay sharp, and come home safe.
      </p>'''
assert old_descriptor in html
html = html.replace(old_descriptor, new_descriptor, 1)
print('1. Hero title line added')

# ── 1b. Hero proof line — add LinkedIn ────────────────────────────────────────
old_proof = '''      <p class="hero-proof">
        10+ years · 33+ courses · Featured in AOPA · Flying · Plane &amp; Pilot · AVweb · EAA Sport Aviation · GA News
      </p>'''
new_proof = '''      <p class="hero-proof">
        10+ years · 33+ courses · Featured in AOPA · Flying · Plane &amp; Pilot · AVweb · EAA Sport Aviation · GA News
      </p>
      <p class="hero-linkedin"><a href="https://linkedin.com/in/harveymadison" target="_blank" rel="noopener">LinkedIn ↗</a></p>'''
assert old_proof in html
html = html.replace(old_proof, new_proof, 1)
print('1b. LinkedIn link added to hero')

# ── 2. GIFT card: add Shorey quote block + stats after adopted pills ───────────
old_impact = '        <p class="project-impact-line">Thousands of copies sold. Hundreds of pilots trained. There\'s a reasonable chance the pilot who flew you home last Thanksgiving learned to fly using GIFT.</p>'
new_impact = '''        <p class="project-impact-line">Thousands of copies sold. Hundreds of pilots trained. There\'s a reasonable chance the pilot who flew you home last Thanksgiving learned to fly using GIFT.</p>

        <div class="project-outcomes">
          <div class="outcome-stat-row">
            <span class="outcome-stat">43 hrs</span>
            <span class="outcome-label">Average time to private pilot certificate at Skyline Aviation — vs. the national average of 67 hours</span>
          </div>
          <div class="outcome-stat-row">
            <span class="outcome-stat">$134–161</span>
            <span class="outcome-label">Per-hour student savings using Redbird AATD vs. training airplane</span>
          </div>
        </div>

        <blockquote class="project-quote">
          <p>"The proof that using GIFT as heavily as we do works can be seen in our time-to-certificate numbers. On average our private pilot students pass their checkrides with only 43 hours in their logbooks. That only happens because of GIFT in our Redbird simulators."</p>
          <cite>— Jonathan Shorey, CEO, Skyline Aviation (Part 61 &amp; Part 141 · Angelo State University)</cite>
        </blockquote>'''
assert old_impact in html
html = html.replace(old_impact, new_impact, 1)
print('2. Shorey quotes and stats added to GIFT card')

# ── 3. GIFT origin story: add to work-intro or after GIFT name ────────────────
old_gift_subtitle = '''        <div class="project-subtitle">Guided Independent Flight Training — Private Pilot</div>
        <div class="project-stat-line">33 modules · One cohesive system · A decade in active use</div>'''
new_gift_subtitle = '''        <div class="project-subtitle">Guided Independent Flight Training — Private Pilot</div>
        <div class="project-origin">Built where four previous attempts failed — including a team that helped build Microsoft Flight Simulator. GIFT shipped 18 months after Harvey joined Redbird. It remains the only product of its kind.</div>
        <div class="project-stat-line">33 modules · One cohesive system · A decade in active use</div>'''
assert old_gift_subtitle in html
html = html.replace(old_gift_subtitle, new_gift_subtitle, 1)
print('3. GIFT origin story added')

# ── 4. About section: add telecom leadership credential + LinkedIn ─────────────
old_creds_end = '''            <span class="cred-text">Webster Trophy — Flight Scenario Challenge Designer &amp; volunteer Board member</span>
          </div>
        </div>'''
new_creds_end = '''            <span class="cred-text">Webster Trophy — Flight Scenario Challenge Designer &amp; volunteer Board member</span>
          </div>
          <div class="cred-row reveal reveal-delay-3">
            <div class="cred-icon">
              <svg viewBox="0 0 12 12"><circle cx="6" cy="6" r="4"/></svg>
            </div>
            <span class="cred-text">Former senior leader, Fortune 500 telecommunications — team of 70+ highly technical staff</span>
          </div>
          <div class="cred-row reveal reveal-delay-3">
            <div class="cred-icon">
              <svg viewBox="0 0 12 12"><circle cx="6" cy="6" r="4"/></svg>
            </div>
            <span class="cred-text"><a href="https://linkedin.com/in/harveymadison" target="_blank" rel="noopener" style="color:var(--sky);">LinkedIn ↗</a></span>
          </div>
        </div>'''
assert old_creds_end in html
html = html.replace(old_creds_end, new_creds_end, 1)
print('4. Telecom leadership + LinkedIn added to About credentials')

# ── 5. Independent projects: reframe intro copy ───────────────────────────────
old_ind_intro = '''        <p class="ind-intro">
          The work Harvey does outside of Redbird isn\'t a side hustle — it\'s the
          same mission running on a different track. When you believe something
          strongly enough, you build toward it on your own time too. These projects
          exist because the GA community needed them, and waiting for someone else
          to build them wasn\'t an option.
        </p>'''
new_ind_intro = '''        <p class="ind-intro">
          This is what passion combined with genuine effectiveness looks like. These projects
          don\'t compete with Harvey\'s career — they extend it. Each one exists because the
          GA community needed it and no one else was building it. That\'s not being scattered.
          That\'s what happens when conviction meets capability and neither one backs down.
        </p>'''
assert old_ind_intro in html
html = html.replace(old_ind_intro, new_ind_intro, 1)
print('5. Independent projects intro reframed')

# ── 6. Copyright: dynamic year via JS ─────────────────────────────────────────
old_copy = '© 2025 Harvey Madison — All rights reserved'
new_copy = '© <span id="copy-year"></span> Harvey Madison — All rights reserved'
assert old_copy in html
html = html.replace(old_copy, new_copy, 1)
# Add year-setting JS to the existing script block
old_script_start = "window.addEventListener('DOMContentLoaded', function() {"
new_script_start = "window.addEventListener('DOMContentLoaded', function() {\n  var yr = document.getElementById('copy-year');\n  if (yr) yr.textContent = new Date().getFullYear();"
assert old_script_start in html
html = html.replace(old_script_start, new_script_start, 1)
print('6. Copyright year made dynamic')

# ── 7. Nav logo: fix white box — use mix-blend-mode instead of invert filter ──
old_nav_css = '.nav-logo-img {  height: 42px;  width: auto;  vertical-align: middle;  filter: brightness(0) invert(1);  opacity: 0.82;  transition: opacity 0.2s;}'
new_nav_css = '.nav-logo-img {  height: 52px;  width: auto;  vertical-align: middle;  mix-blend-mode: screen;  opacity: 0.88;  transition: opacity 0.2s;}'
assert old_nav_css in html
html = html.replace(old_nav_css, new_nav_css, 1)
print('7. Nav logo CSS fixed')

# ── 8. Add CSS for new elements ───────────────────────────────────────────────
old_btn_css = '''.btn {
  font-family: var(--font-display);
  font-weight: 700;'''
new_btn_css = '''/* Hero title credential line */
.hero-title-line {
  font-family: var(--font-display);
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--sky);
  margin-bottom: 18px;
  opacity: 0.85;
}

/* Hero LinkedIn link */
.hero-linkedin {
  margin-bottom: 28px;
  margin-top: -8px;
}
.hero-linkedin a {
  font-family: var(--font-display);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--sky);
  opacity: 0.7;
  transition: opacity 0.2s;
}
.hero-linkedin a:hover { opacity: 1; }

/* GIFT origin story tag */
.project-origin {
  font-family: var(--font-body);
  font-size: 0.82rem;
  font-style: italic;
  color: var(--amber);
  line-height: 1.55;
  margin-bottom: 14px;
  opacity: 0.85;
  padding-left: 12px;
  border-left: 2px solid var(--amber);
}

/* Outcome stats block */
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
  font-size: 1.4rem;
  color: var(--amber);
  white-space: nowrap;
  flex-shrink: 0;
}
.outcome-label {
  font-family: var(--font-body);
  font-size: 0.85rem;
  color: var(--mist);
  line-height: 1.45;
  opacity: 0.8;
}

/* Shorey quote block */
.project-quote {
  margin-top: 20px;
  padding: 18px 20px;
  border-left: 3px solid rgba(46,143,168,0.4);
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
assert old_btn_css in html
html = html.replace(old_btn_css, new_btn_css, 1)
print('8. New CSS added')

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)
print('All done. Length:', len(html))
