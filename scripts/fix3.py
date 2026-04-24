
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# ─── FIX 1: Airfoil — level (remove rotation), move down 100px ───────────────
html = html.replace(
    '<!-- Googie aviation accent: NACA airfoil, 45 degree climb attitude -->\n        <svg viewBox="-20 -130 460 470" xmlns="http://www.w3.org/2000/svg"\n             style="width:100%;margin-top:24px;display:block;" opacity="0.58">\n          <g transform="rotate(-45, 200, 97)">',
    '<!-- Googie aviation accent: NACA airfoil with laminar flow -->\n        <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg"\n             style="width:100%;margin-top:124px;display:block;" opacity="0.58">\n          <g>'
)
print('Fix 1 airfoil:', 'margin-top:124px' in html)

# ─── FIX 2: Runway — place after speaking-grid, on dark background, 200px margin ─
# The runway SVG was removed — we need to re-add it fresh
# It goes after speaking-grid closes (    </div>) before section-inner closes (  </div>)

runway_svg = '''
        <!-- Googie aviation accent: runway low-angle perspective -->
        <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg"
             style="width:100%;margin-top:200px;display:block;" opacity="0.52">
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

# Insert after speaking-grid close (    </div>) and before section-inner close (  </div>)
old_end = '      </div>\n\n    </div>\n  </div>\n</section>\n\n<!-- ═══ CONTACT'
new_end = '      </div>\n\n    </div>\n' + runway_svg + '\n  </div>\n</section>\n\n<!-- ═══ CONTACT'

assert old_end in html, f'End pattern not found! Looking for: {repr(old_end[:60])}'
html = html.replace(old_end, new_end, 1)
print('Fix 2 runway placed after speaking-grid:', 'margin-top:200px' in html)

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)
print('Done. Length:', len(html))
