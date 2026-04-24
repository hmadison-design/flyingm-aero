
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# Step 1: Remove runway from wherever it currently is
rw_marker = '<!-- Googie aviation accent: runway low-angle perspective -->'
if rw_marker in html:
    i1 = html.find(rw_marker)
    # back up to get preceding newlines/whitespace
    while i1 > 0 and html[i1-1] in ' \t\n': i1 -= 1
    i2 = html.find('</svg>', i1) + len('</svg>')
    if html[i2:i2+1] == '\n': i2 += 1
    html = html[:i1] + html[i2:]
    print('Runway removed from current location')
else:
    print('Runway not found - will just insert fresh')

# Step 2: Find the speaking-grid structure and wrap right column
# Current: <div class="speaking-topics reveal reveal-delay-1">...</div>  (right col)
# New: <div class="speaking-right-col"><div class="speaking-topics...">...</div> + runway SVG</div>

old_topics_open = '<div class="speaking-topics reveal reveal-delay-1">'
# Find the closing </div> of speaking-topics — it's followed by closing speaking-grid, section-inner, section
# Pattern after speaking-topics closes: \n\n    </div>\n  </div>\n</section>
old_topics_close = '      </div>\n\n    </div>\n  </div>\n</section>\n\n<!-- ═══ CONTACT'

assert old_topics_open in html, 'speaking-topics open not found'
assert old_topics_close in html, f'speaking-topics close not found'

runway_svg = '''        <!-- Googie aviation accent: runway low-angle perspective -->
        <svg viewBox="0 0 380 210" xmlns="http://www.w3.org/2000/svg"
             style="width:100%;margin-top:24px;display:block;" opacity="0.52">
          <polygon points="20,205 360,205 190,18" fill="rgba(46,143,168,0.09)" stroke="#3a9ab8" stroke-width="1.4"/>
          <line x1="190" y1="197" x2="190" y2="178" stroke="#e8a030" stroke-width="2.5" opacity="0.7"/>
          <line x1="190" y1="168" x2="190" y2="149" stroke="#e8a030" stroke-width="2"   opacity="0.65"/>
          <line x1="190" y1="139" x2="190" y2="120" stroke="#e8a030" stroke-width="1.5" opacity="0.55"/>
          <line x1="190" y1="110" x2="190" y2="93"  stroke="#e8a030" stroke-width="1.2" opacity="0.45"/>
          <line x1="190" y1="83"  x2="190" y2="68"  stroke="#e8a030" stroke-width="0.8" opacity="0.35"/>
          <circle cx="30"  cy="197" r="3"   fill="#7ecfe6" opacity="0.85"/>
          <circle cx="49"  cy="178" r="2.5" fill="#7ecfe6" opacity="0.75"/>
          <circle cx="74"  cy="153" r="2"   fill="#7ecfe6" opacity="0.65"/>
          <circle cx="99"  cy="128" r="1.8" fill="#7ecfe6" opacity="0.55"/>
          <circle cx="121" cy="104" r="1.4" fill="#7ecfe6" opacity="0.45"/>
          <circle cx="143" cy="80"  r="1"   fill="#7ecfe6" opacity="0.35"/>
          <circle cx="350" cy="197" r="3"   fill="#7ecfe6" opacity="0.85"/>
          <circle cx="331" cy="178" r="2.5" fill="#7ecfe6" opacity="0.75"/>
          <circle cx="306" cy="153" r="2"   fill="#7ecfe6" opacity="0.65"/>
          <circle cx="281" cy="128" r="1.8" fill="#7ecfe6" opacity="0.55"/>
          <circle cx="259" cy="104" r="1.4" fill="#7ecfe6" opacity="0.45"/>
          <circle cx="237" cy="80"  r="1"   fill="#7ecfe6" opacity="0.35"/>
          <line x1="0" y1="18" x2="380" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.4" stroke-dasharray="4,7"/>
          <g transform="translate(190,14)">
            <polygon points="0,-7 -1.5,-2 -13,0 -1.5,2 0,7 1.5,2 13,0 1.5,-2" fill="#e8a030" opacity="0.85"/>
          </g>
          <line x1="5"   y1="120" x2="190" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.25"/>
          <line x1="5"   y1="150" x2="190" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.20"/>
          <line x1="5"   y1="180" x2="190" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.15"/>
          <line x1="375" y1="120" x2="190" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.25"/>
          <line x1="375" y1="150" x2="190" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.20"/>
          <line x1="375" y1="180" x2="190" y2="18" stroke="#3a9ab8" stroke-width="0.8" opacity="0.15"/>
          <line x1="20" y1="205" x2="360" y2="205" stroke="#7ecfe6" stroke-width="3" opacity="0.65"/>
          <g transform="translate(22,168)" opacity="0.45">
            <polygon points="0,-14 1.8,-4.5 9,-9 4.5,-1.5 14,0 4.5,1.5 9,9 1.8,4.5 0,14 -1.8,4.5 -9,9 -4.5,1.5 -14,0 -4.5,-1.5 -9,-9 -1.8,-4.5" fill="#e8a030"/>
          </g>
          <g transform="translate(358,168)" opacity="0.38">
            <polygon points="0,-11 1.4,-3.5 7,-7 3.5,-1 11,0 3.5,1 7,7 1.4,3.5 0,11 -1.4,3.5 -7,7 -3.5,1 -11,0 -3.5,-1 -7,-7 -1.4,-3.5" fill="#e8a030"/>
          </g>
          <text x="128" y="222" font-family="'Barlow Condensed',sans-serif" font-size="8"
                fill="#7ecfe6" font-weight="400" letter-spacing="2" opacity="0.4">RUNWAY 18 - CLEARED FOR TAKEOFF</text>
        </svg>'''

# Wrap the speaking-topics div + runway in a right-col wrapper
new_topics_open = '<div class="speaking-right-col">\n      ' + old_topics_open
new_topics_close = '      </div>\n\n' + runway_svg + '\n\n    </div><!-- end speaking-right-col -->\n  </div>\n</section>\n\n<!-- ═══ CONTACT'

html = html.replace(old_topics_open, new_topics_open, 1)
html = html.replace(old_topics_close, new_topics_close, 1)
print('Wrapper and runway inserted')

# Step 3: Add CSS for speaking-right-col (after speaking-topics CSS block)
old_css = '.speaking-topics {\n  background: var(--deep);\n  border: 1px solid rgba(200,223,230,0.1);\n  padding: 40px;\n}'
new_css = '''.speaking-topics {
  background: var(--deep);
  border: 1px solid rgba(200,223,230,0.1);
  padding: 40px;
}

.speaking-right-col {
  display: flex;
  flex-direction: column;
}'''

if old_css in html:
    html = html.replace(old_css, new_css, 1)
    print('CSS added for speaking-right-col')
else:
    print('WARNING: speaking-topics CSS not found, adding inline style instead')
    html = html.replace(
        '<div class="speaking-right-col">',
        '<div class="speaking-right-col" style="display:flex;flex-direction:column;">'
    )
    print('Inline style added as fallback')

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)
print('Done. Length:', len(html))
