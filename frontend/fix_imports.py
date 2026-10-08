import os
import re

base_dir = "d:/Projects/ai_color_desinger/frontend/src/pages"

for file in ["Projects.tsx", "Upload.tsx", "Dashboard.tsx", "Profile.tsx", "Results.tsx"]:
    filepath = os.path.join(base_dir, file)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix import syntax
    if "import React\nimport { useTranslation } from 'react-i18next';," in content:
        content = content.replace("import React\nimport { useTranslation } from 'react-i18next';,", "import React,")
        content = "import { useTranslation } from 'react-i18next';\n" + content
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
print("Imports fixed.")
