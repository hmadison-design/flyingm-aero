
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# ─── FIX 1: Airfoil — remove rotation, fix viewBox, move down 100px ──────────
html = html.replace(
    '<!-- Googie aviation accent: NACA airfoil, 45 degree climb attitude -->        <svg viewBox="-20 -130 460 470" xmlns="http://www.w3.org/2000/svg"             style="width:100%;margin-top:24px;display:block;" opacity="0.58">          <g transform="rotate(-45, 200, 97)">',
    '<!-- Googie aviation accent: NACA airfoil with laminar flow -->        <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg"             style="width:100%;margin-top:124px;display:block;" opacity="0.58">          <g>'
)
print('Fix 1 airfoil done:', '124px' in html)

# ─── FIX 2: Runway — remove from speaking-topics, place after grid, margin 200px ─
# Step A: Remove runway SVG from inside speaking-topics
rw_start = '\n        <!-- Googie aviation accent: runway low-angle perspective -->'
rw_end_marker = 'RUNWAY 18 - CLEARED FOR TAKEOFF</text>\n        </svg>'

i1 = html.find(rw_start)
i2 = html.find(rw_end_marker) + len(rw_end_marker)
# Consume trailing newline
if html[i2:i2+1] == '\n': i2 += 1

runway_svg_block = html[i1:i2]
html = html[:i1] + html[i2:]
print('Runway removed from speaking-topics, length:', len(html))

# Update the runway SVG margin-top to 200px (from existing 32px)
runway_svg_block = runway_svg_block.replace(
    'style="width:100%;margin-top:32px;display:block;"',
    'style="width:100%;margin-top:200px;display:block;"'
)

# Step B: Insert runway AFTER the speaking-grid div closes, inside section-inner
# The speaking-grid is followed by section-inner close, then section close
# Structure: </div>  (speaking-grid) </div> (section-inner) </section>
# Find the end of speaking-grid: it contains two child divs (left + speaking-topics)
# After removing runway from speaking-topics, speaking-topics ends with last topic row </div>
# Then speaking-grid closes, then section-inner closes

# Find the sequence: speaking-topics close -> speaking-grid close
search = '      </div>    </div>  </div></section><!-- '
i_grid_end = html.find(search)
if i_grid_end == -1:
    # Try to find it differently - look for end of speaking section
    search2 = '      </div>    </div>  </div></section>'
    i_grid_end = html.find(search2)
    print(f'Using search2, found at: {i_grid_end}')
else:
    print(f'Found grid end at: {i_grid_end}')

if i_grid_end != -1:
    # Insert after the speaking-topics closing div (first </div> in the sequence)
    # The sequence is: speaking-topics-close + speaking-grid-close + section-inner-close + section-close
    # We want: speaking-topics-close + runway + speaking-grid-close + section-inner-close + section-close
    insert_after = '      </div>'  # speaking-topics closing div
    insert_pos = i_grid_end + len(insert_after)
    html = html[:insert_pos] + runway_svg_block + html[insert_pos:]
    print('Runway inserted after speaking-topics, before speaking-grid close')
else:
    # Last resort: find section speaking close
    print('Trying to find by speaking section content...')
    # Find speaking-topics and the divs that follow
    st_idx = html.rfind('</div>', 0, html.find('</section>', html.find('id="speaking"')))
    print(f'Speaking section div end at: {st_idx}')
    print(repr(html[st_idx-50:st_idx+100]))

with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'w') as f:
    f.write(html)
print('All done. Length:', len(html))
