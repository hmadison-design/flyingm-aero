
with open('/Users/harveymadison/Downloads/Website Redesign/site/index.html', 'r') as f:
    html = f.read()

# Find the speaking section and print its closing structure
i_speaking = html.find('id="speaking"')
i_contact = html.find('<!-- ═══ CONTACT')
speaking_section = html[i_speaking:i_contact]

# Print last 600 chars to see full closing structure
print('END OF SPEAKING SECTION:')
print(repr(speaking_section[-600:]))
