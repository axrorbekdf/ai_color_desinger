import re

filepath = r"d:\Projects\ai_color_desinger\frontend\src\pages\Upload.tsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the missing 'e' in event handlers where 'e.something' is used but 'e' is not defined
content = re.sub(r'onClick={\(\) => {\s*e\.stopPropagation\(\);', r'onClick={(e) => { e.stopPropagation();', content)
content = re.sub(r'onDragOver={\(\) => {\s*e\.preventDefault\(\);', r'onDragOver={(e) => { e.preventDefault();', content)
content = re.sub(r'onDragLeave={\(\) => {\s*e\.preventDefault\(\);', r'onDragLeave={(e) => { e.preventDefault();', content)
content = re.sub(r'onDrop={\(\) => {\s*e\.preventDefault\(\);', r'onDrop={(e) => { e.preventDefault();', content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed e in Upload")
