import re
import html

with open('ADI.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<td class="line-content">(.*?)</td>', content, re.DOTALL)

fixed_lines = []
for match in matches:
    text_content = re.sub(r'<[^>]+>', '', match)
    decoded_line = html.unescape(text_content)
    fixed_lines.append(decoded_line)

fixed_html = "\n".join(fixed_lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed_html)

print("Created adi.fixed.html with the corrected HTML content.")

