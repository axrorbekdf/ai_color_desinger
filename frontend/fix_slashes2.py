with open('src/pages/Upload.tsx', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(r"\'upload.ai_recommendations\'", "'upload.ai_recommendations'")
c = c.replace(r"\'upload.design_style_upload\'", "'upload.design_style_upload'")
c = c.replace(r"\'upload.summary\'", "'upload.summary'")

with open('src/pages/Upload.tsx', 'w', encoding='utf-8') as f:
    f.write(c)
