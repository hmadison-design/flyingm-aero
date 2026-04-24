
import re

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# ─── SVG 1: AIRFOIL — rotate -45°, scale up ───────────────────────────────
airfoil_start = '        <!-- Googie aviation accent: NACA airfoil with laminar flow -->'
i1 = html.index(airfoil_start)
i2 = html.index('</svg>', i1) + len('</svg>')
html = html[:i1] + '''        <!-- Googie aviation accent: NACA airfoil, 45 degree climb attitude -->
        <svg viewBox="-20 -130 460 470" xmlns="http://www.w3.org/2000/svg"
             style="width:100%;margin-top:24px;display:block;" opacity="0.58">
          <g transform="rotate(-45, 200, 97)">
            <path d="M 0,28 C 80,26 200,20 400,30" fill="none" stroke="#7ecfe6" stroke-width="1"/>
            <path d="M 0,46 C 80,42 200,34 400,48" fill="none" stroke="#7ecfe6" stroke-width="1.2"/>
            <path d="M 0,66 C 50,56 90,42 180,40 C 270,40 330,54 400,68" fill="none" stroke="#3a9ab8" stroke-width="1.8"/>
            <path d="M 38,98 C 95,52 235,47 385,94 C 235,106 95,108 38,98 Z"
                  fill="rgba(46,143,168,0.12)" stroke="#3a9ab8" stroke-width="2.4"/>
            <line x1="38" y1="98" x2="385" y2="98" stroke="#7ecfe6" stroke-width="0.9"
                  stroke-dasharray="6,5" opacity="0.45"/>
            <path d="M 0,128 C 60,118 100,115 200,114 C 300,115 360,122 400,130" fill="none" stroke="#3a9ab8" stroke-width="1.8"/>
            <path d="M 0,152 C 120,148 260,146 400,152" fill="none" stroke="#7ecfe6" stroke-width="1.2"/>
            <path d="M 0,170 C 120,167 260,165 400,170" fill="none" stroke="#7ecfe6" stroke-width="1"/>
            <line x1="210" y1="69" x2="210" y2="14" stroke="#e8a030" stroke-width="2"/>
            <polygon points="210,2 201,20 219,20" fill="#e8a030"/>
            <circle cx="38" cy="98" r="5" fill="#7ecfe6" opacity="0.9"/>
            <line x1="120" y1="60" x2="120" y2="47" stroke="#e8a030" stroke-width="1.2" opacity="0.65"/>
            <line x1="200" y1="50" x2="200" y2="37" stroke="#e8a030" stroke-width="1.2" opacity="0.65"/>
            <line x1="280" y1="58" x2="280" y2="45" stroke="#e8a030" stroke-width="1.2" opacity="0.65"/>
            <text x="220" y="10" font-family="'Barlow Condensed',sans-serif" font-size="12"
                  fill="#e8a030" font-weight="700" letter-spacing="2">LIFT</text>
            <text x="162" y="93" font-family="'Barlow Condensed',sans-serif" font-size="9"
                  fill="#7ecfe6" font-weight="400" letter-spacing="1.5" opacity="0.5">CHORD LINE</text>
            <text x="0" y="192" font-family="'Barlow Condensed',sans-serif" font-size="9"
                  fill="#7ecfe6" font-weight="400" letter-spacing="1.5" opacity="0.4">NACA SECTION - LAMINAR FLOW</text>
          </g>
        </svg>''' + html[i2:]
print('SVG 1 airfoil done, html length:', len(html))


# ─── SVG 2: HEADING INDICATOR — 2x scale, lubber triangle, heading bug ──────
hi_start = '        <!-- Googie aviation accent: heading indicator dial -->'
i1 = html.index(hi_start)
i2 = html.index('</svg>', i1) + len('</svg>')
html = html[:i1] + '''        <!-- Googie aviation accent: heading indicator dial -->
        <svg viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg"
             style="width:100%;max-width:320px;margin-top:28px;display:block;" opacity="0.58">
          <circle cx="160" cy="160" r="140" fill="none" stroke="#3a9ab8" stroke-width="2"/>
          <circle cx="160" cy="160" r="128" fill="rgba(11,45,58,0.4)" stroke="#3a9ab8" stroke-width="1" opacity="0.5"/>
          <g stroke="#7ecfe6" stroke-width="2">
            <line x1="160" y1="20"   x2="160" y2="34"/>
            <line x1="230" y1="38.8" x2="224.3" y2="50.5"/>
            <line x1="281.2" y1="90"  x2="270.1" y2="96.4"/>
            <line x1="300" y1="160"  x2="286" y2="160"/>
            <line x1="281.2" y1="230" x2="270.1" y2="223.6"/>
            <line x1="230" y1="281.2" x2="224.3" y2="269.5"/>
            <line x1="160" y1="300"  x2="160" y2="286"/>
            <line x1="90"  y1="281.2" x2="95.7" y2="269.5"/>
            <line x1="38.8" y1="230" x2="49.9" y2="223.6"/>
            <line x1="20"  y1="160"  x2="34"  y2="160"/>
            <line x1="38.8" y1="90"  x2="49.9" y2="96.4"/>
            <line x1="90"  y1="38.8" x2="95.7" y2="50.5"/>
          </g>
          <g stroke="#3a9ab8" stroke-width="1" opacity="0.75">
            <line x1="184.4" y1="22.1" x2="183.3" y2="27.9"/>
            <line x1="207.9" y1="28.4" x2="205.8" y2="33.9"/>
            <line x1="250.0" y1="52.8" x2="246.2" y2="57.4"/>
            <line x1="267.2" y1="70.0" x2="262.6" y2="73.8"/>
            <line x1="291.6" y1="112.1" x2="285.9" y2="114.2"/>
            <line x1="297.9" y1="135.6" x2="291.9" y2="136.7"/>
            <line x1="297.9" y1="184.4" x2="291.9" y2="183.3"/>
            <line x1="291.6" y1="207.9" x2="285.9" y2="205.8"/>
            <line x1="267.2" y1="250.0" x2="262.6" y2="246.2"/>
            <line x1="250.0" y1="267.2" x2="246.2" y2="262.6"/>
            <line x1="207.9" y1="291.6" x2="205.8" y2="285.9"/>
            <line x1="184.4" y1="297.9" x2="183.3" y2="291.9"/>
            <line x1="135.6" y1="297.9" x2="136.7" y2="291.9"/>
            <line x1="112.1" y1="291.6" x2="114.2" y2="285.9"/>
            <line x1="70.0"  y1="267.2" x2="73.8"  y2="262.6"/>
            <line x1="52.8"  y1="250.0" x2="57.4"  y2="246.2"/>
            <line x1="28.4"  y1="207.9" x2="33.9"  y2="205.8"/>
            <line x1="22.1"  y1="184.4" x2="27.9"  y2="183.3"/>
            <line x1="22.1"  y1="135.6" x2="27.9"  y2="136.7"/>
            <line x1="28.4"  y1="112.1" x2="33.9"  y2="114.2"/>
            <line x1="52.8"  y1="70.0"  x2="57.4"  y2="73.8"/>
            <line x1="70.0"  y1="52.8"  x2="73.8"  y2="57.4"/>
            <line x1="112.1" y1="28.4"  x2="114.2" y2="33.9"/>
            <line x1="135.6" y1="22.1"  x2="136.7" y2="27.9"/>
          </g>
          <text x="160" y="58" text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="20" fill="#7ecfe6" font-weight="700">N</text>
          <text x="160" y="276" text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="20" fill="#3a9ab8" font-weight="700">S</text>
          <text x="274" y="166" text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="20" fill="#3a9ab8" font-weight="700">E</text>
          <text x="46"  y="166" text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="20" fill="#3a9ab8" font-weight="700">W</text>
          <text x="217.5" y="62.5" text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">3</text>
          <text x="259.5" y="104"  text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">6</text>
          <text x="259.5" y="218"  text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">12</text>
          <text x="217.5" y="260"  text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">15</text>
          <text x="102.5" y="260"  text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">21</text>
          <text x="60.5"  y="218"  text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">24</text>
          <text x="60.5"  y="104"  text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">30</text>
          <text x="102.5" y="62.5" text-anchor="middle" font-family="'Barlow Condensed',sans-serif" font-size="11" fill="#7ecfe6" opacity="0.65">33</text>
          <!-- Lubber line: solid orange downward triangle at 12 o-clock -->
          <polygon points="150,8 170,8 160,26" fill="#e8a030" opacity="0.95"/>
          <line x1="160" y1="26" x2="160" y2="40" stroke="#e8a030" stroke-width="2.5" opacity="0.7"/>
          <!-- Heading bug at 060 degrees - classic U-clamp straddling the ring -->
          <g transform="rotate(60, 160, 160)" opacity="0.9">
            <line x1="150" y1="10" x2="170" y2="10" stroke="#e8a030" stroke-width="4.5" stroke-linecap="square"/>
            <line x1="150" y1="10" x2="150" y2="30" stroke="#e8a030" stroke-width="4.5" stroke-linecap="square"/>
            <line x1="170" y1="10" x2="170" y2="30" stroke="#e8a030" stroke-width="4.5" stroke-linecap="square"/>
          </g>
          <!-- South tail -->
          <polygon points="160,286 155,268 160,272 165,268" fill="#3a9ab8" opacity="0.5"/>
          <!-- Center reference -->
          <circle cx="160" cy="160" r="8" fill="none" stroke="#7ecfe6" stroke-width="2"/>
          <line x1="160" y1="108" x2="160" y2="152" stroke="#7ecfe6" stroke-width="2" opacity="0.8"/>
          <line x1="160" y1="168" x2="160" y2="212" stroke="#7ecfe6" stroke-width="1.5" opacity="0.4"/>
          <line x1="108" y1="160" x2="152" y2="160" stroke="#7ecfe6" stroke-width="1.5" opacity="0.5"/>
          <line x1="168" y1="160" x2="212" y2="160" stroke="#7ecfe6" stroke-width="1.5" opacity="0.5"/>
          <!-- Starburst -->
          <g transform="translate(296,28)" opacity="0.5">
            <polygon points="0,-16 2,-5.5 9,-9 5,-2 16,0 5,2 9,9 2,5.5 0,16 -2,5.5 -9,9 -5,2 -16,0 -5,-2 -9,-9 -2,-5.5" fill="#e8a030"/>
          </g>
        </svg>''' + html[i2:]
print('SVG 2 heading indicator done, html length:', len(html))


# ─── SVG 3: RUNWAY — remove contrails, converge to point, widen base ────────
# Remove old runway SVG from inside speaking-topics
rw_start = '        <!-- Googie aviation accent: runway perspective with contrails -->'
i1 = html.index(rw_start)
i2 = html.index('</svg>', i1) + len('</svg>')
if html[i2:i2+1] == '\n': i2 += 1
html = html[:i1] + html[i2:]
print('Old runway SVG removed')

new_runway = '''
        <!-- Googie aviation accent: runway low-angle perspective -->
        <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg"
             style="width:100%;margin-top:32px;display:block;" opacity="0.52">
          <polygon points="45,200 335,200 190,30" fill="rgba(46,143,168,0.09)" stroke="#3a9ab8" stroke-width="1.4"/>
          <line x1="190" y1="192" x2="190" y2="172" stroke="#e8a030" stroke-width="2.5" opacity="0.7"/>
          <line x1="190" y1="162" x2="190" y2="142" stroke="#e8a030" stroke-width="2"   opacity="0.65"/>
          <line x1="190" y1="132" x2="190" y2="112" stroke="#e8a030" stroke-width="1.5" opacity="0.55"/>
          <line x1="190" y1="102" x2="190" y2="86"  stroke="#e8a030" stroke-width="1.2" opacity="0.45"/>
          <line x1="190" y1="76"  x2="190" y2="62"  stroke="#e8a030" stroke-width="0.8" opacity="0.35"/>
          <circle cx="55"  cy="187" r="3"   fill="#7ecfe6" opacity="0.85"/>
          <circle cx="71"  cy="170" r="2.5" fill="#7ecfe6" opacity="0.75"/>
          <circle cx="95"  cy="147" r="2"   fill="#7ecfe6" opacity="0.65"/>
          <circle cx="118" cy="124" r="1.8" fill="#7ecfe6" opacity="0.55"/>
          <circle cx="140" cy="101" r="1.4" fill="#7ecfe6" opacity="0.45"/>
          <circle cx="161" cy="78"  r="1"   fill="#7ecfe6" opacity="0.35"/>
          <circle cx="325" cy="187" r="3"   fill="#7ecfe6" opacity="0.85"/>
          <circle cx="309" cy="170" r="2.5" fill="#7ecfe6" opacity="0.75"/>
          <circle cx="285" cy="147" r="2"   fill="#7ecfe6" opacity="0.65"/>
          <circle cx="262" cy="124" r="1.8" fill="#7ecfe6" opacity="0.55"/>
          <circle cx="240" cy="101" r="1.4" fill="#7ecfe6" opacity="0.45"/>
          <circle cx="219" cy="78"  r="1"   fill="#7ecfe6" opacity="0.35"/>
          <line x1="0" y1="30" x2="380" y2="30" stroke="#3a9ab8" stroke-width="0.8" opacity="0.45" stroke-dasharray="4,7"/>
          <g transform="translate(190,26)">
            <polygon points="0,-8 -1.5,-2 -14,0 -1.5,2 0,8 1.5,2 14,0 1.5,-2" fill="#e8a030" opacity="0.85"/>
          </g>
          <line x1="5"   y1="130" x2="190" y2="30" stroke="#3a9ab8" stroke-width="0.9" opacity="0.28"/>
          <line x1="5"   y1="160" x2="190" y2="30" stroke="#3a9ab8" stroke-width="0.9" opacity="0.22"/>
          <line x1="5"   y1="190" x2="190" y2="30" stroke="#3a9ab8" stroke-width="0.9" opacity="0.17"/>
          <line x1="375" y1="130" x2="190" y2="30" stroke="#3a9ab8" stroke-width="0.9" opacity="0.28"/>
          <line x1="375" y1="160" x2="190" y2="30" stroke="#3a9ab8" stroke-width="0.9" opacity="0.22"/>
          <line x1="375" y1="190" x2="190" y2="30" stroke="#3a9ab8" stroke-width="0.9" opacity="0.17"/>
          <line x1="45" y1="200" x2="335" y2="200" stroke="#7ecfe6" stroke-width="3" opacity="0.65"/>
          <g transform="translate(22,162)" opacity="0.45">
            <polygon points="0,-16 2,-5 10,-10 5,-1.5 16,0 5,1.5 10,10 2,5 0,16 -2,5 -10,10 -5,1.5 -16,0 -5,-1.5 -10,-10 -2,-5" fill="#e8a030"/>
          </g>
          <g transform="translate(358,162)" opacity="0.38">
            <polygon points="0,-13 1.6,-4 8,-8 4,-1 13,0 4,1 8,8 1.6,4 0,13 -1.6,4 -8,8 -3.5,1 -13,0 -3.5,-1 -8,-8 -1.6,-4" fill="#e8a030"/>
          </g>
          <text x="135" y="218" font-family="'Barlow Condensed',sans-serif" font-size="8"
                fill="#7ecfe6" font-weight="400" letter-spacing="2" opacity="0.45">RUNWAY 18 - CLEARED FOR TAKEOFF</text>
        </svg>'''

# Insert runway SVG AFTER the speaking-topics closing div, BEFORE speaking-grid closes
# speaking-topics ends with its last topic-row div, then </div>
# Then speaking-grid closes with </div>, then section-inner with </div>, then </section>
# Pattern: ...topic 06 row...</div>\n      </div>\n\n    </div>
# We want to insert between the speaking-topics </div> and the speaking-grid </div>

# Find last topic row and the divs that follow
target = '      </div>\n\n    </div>\n  </div>\n</section>\n<!-- \'\'\'= CONTACT'
# Actually search for the pattern in the file
search = '      </div>\n\n    </div>\n  </div>\n</section>'
idx = html.find(search)
if idx == -1:
    search = '      </div>\n    </div>\n  </div>\n</section>'
    idx = html.find(search)

if idx != -1:
    # Insert after the first </div> (closing speaking-topics)
    first_close = idx + len('      </div>\n')
    html = html[:first_close] + new_runway + '\n' + html[first_close:]
    print('SVG 3 inserted, html length:', len(html))
else:
    print('ERROR: insertion point not found, searching context...')
    i = html.find('FAA WINGS safety courses')
    print(repr(html[i:i+400]))

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)
print('All done. File saved.')
