
import subprocess
result = subprocess.run(
    ['grep', '-n', 'nav-logo-img\|footer-copy\|project-impact-line\|about-credentials\|ind-intro\|2025 Harvey\|hero-eyebrow\|hero-proof\|project-adopted',
     '/Users/harveymadison/Downloads/Website Redesign/site/index.html'],
    capture_output=True, text=True
)
print(result.stdout)
