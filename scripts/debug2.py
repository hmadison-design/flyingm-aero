
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# Current minified structure after topic 06:
# ...checkbox</span>        </div>      </div>    </div>        <!-- Googie...runway...200px...svg>  </div></section>
#
# Breakdown:
#   </div>  = topic-row close
#   </div>  = speaking-topics close  
#   </div>  = speaking-grid close
#   <!-- Googie...svg>  = runway at section-inner level (WRONG - full width)
#   </div>  = section-inner close
# </section> = speaking section close
#
# Goal: wrap speaking-topics + runway in a div that IS the right grid column
# New structure:
#   </div>  = topic-row close
#   </div>  = speaking-topics close
#   [runway SVG here]
#   </div>  = right-col wrapper close  
#   </div>  = speaking-grid close
#   </div>  = section-inner close
# </section>

# Find the old runway SVG block
old_rw_start = '        <!-- Googie aviation accent: runway low-angle perspective -->'
old_rw_end = 'CLEARED FOR TAKEOFF</text>\n        </svg>'
i1 = html.find(old_rw_start)
i2 = html.find(old_rw_end) + len(old_rw_end)

# Find what comes after the runway SVG  
print('After runway:', repr(html[i2:i2+60]))

# The sequence we need to find and replace is:
# [speaking-topics close] + [speaking-grid close] + [runway SVG] + [section-inner close]
# We want:
# [speaking-topics close] + [runway SVG] + [wrapper close] + [speaking-grid close] + [section-inner close]

# The speaking-topics close + grid close in minified form is:
topics_and_grid_close = '      </div>\n    </div>\n        <!-- Googie aviation accent: runway low-angle perspective -->'

if topics_and_grid_close in html:
    print('Found topics+grid close pattern')
else:
    # Try to find what's between topic 06 and runway
    i_06 = html.find('CLEARED FOR TAKEOFF')
    before_runway = html[html.find('FAA WINGS safety courses'):i1]
    print('Between 06 and runway:', repr(before_runway[-100:]))
EOF
