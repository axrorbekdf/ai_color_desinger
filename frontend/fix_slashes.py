import os

for root, dirs, files in os.walk(r"d:\Projects\ai_color_desinger\frontend\src\pages"):
    for fname in files:
        if fname.endswith(".tsx"):
            path = os.path.join(root, fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = content.replace("\\'react-i18next\\'", "'react-i18next'")
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
print("Fixed slashes")
