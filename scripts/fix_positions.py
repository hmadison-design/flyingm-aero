
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# ─── FIX 1: Heading indicator — remove max-width so it fills the column ──────
old_hi_style = 'style="width:100%;max-width:320px;margin-top:28px;display:block;" opacity="0.58"'
new_hi_style = 'style="width:100%;margin-top:28px;display:block;" opacity="0.58"'
assert old_hi_style in html, 'HI style not found'
html = html.replace(old_hi_style, new_hi_style, 1)
print('Fix 1 heading indicator size done')

# ─── FIX 2: Runway — move back inside speaking-topics div ────────────────────
# The runway is currently after speaking-topics div close, before speaking-grid close
# Find and remove it from its current wrong location
runway_start = '\n        <!-- Googie aviation accent: runway low-angle perspective -->'
runway_end_marker = 'RUNWAY 18 - CLEARED FOR TAKEOFF</text>\n        </svg>'
i1 = html.find(runway_start)
i2 = html.find(runway_end_marker) + len(runway_end_marker)
# Consume trailing newline
if html[i2:i2+1] == '\n': i2 += 1

runway_svg = html[i1:i2]
html = html[:i1] + html[i2:]
print('Runway removed from wrong location, length now:', len(html))

# Now insert back inside speaking-topics div, after the last topic row (06)
topic_06_end = '          <span class="topic-text">FAA WINGS safety courses \u2014 proficiency as a practice, not a checkbox</span>\n        </div>'
assert topic_06_end in html, 'topic 06 not found'
html = html.replace(topic_06_end, topic_06_end + '\n' + runway_svg, 1)
print('Runway inserted back inside speaking-topics')

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)
print('Done. Length:', len(html))
