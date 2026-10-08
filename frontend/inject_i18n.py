import os
import re

base_dir = "d:/Projects/ai_color_desinger/frontend/src/pages"

def fix_imports_and_hooks(files):
    for f in files:
        filepath = os.path.join(base_dir, f)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        if "useTranslation" not in content:
            content = "import { useTranslation } from 'react-i18next';\n" + content
            content = re.sub(r'export const (\w+) = \(\) => {', r'export const \1 = () => {\n  const { t } = useTranslation();', content)
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

fix_imports_and_hooks(["Projects.tsx", "Upload.tsx", "Dashboard.tsx", "Profile.tsx", "Results.tsx", "About.tsx", "AiAnalysis.tsx", "ColorRec.tsx", "MoodAnalysis.tsx", "DesignStyle.tsx"])

print("Injected useTranslation")
