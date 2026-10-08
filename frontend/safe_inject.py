import os
import re

base_dir = r"d:\Projects\ai_color_desinger\frontend\src\pages"

def safe_inject_i18n(files):
    for f in files:
        path = os.path.join(base_dir, f)
        if not os.path.exists(path): continue
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            
        if "useTranslation" not in content:
            # inject import after the first import
            content = re.sub(r'(import .*?;)', r'\1\nimport { useTranslation } from \'react-i18next\';', content, count=1)
            # inject hook inside component
            content = re.sub(r'export const (\w+) = \(\) => {', r'export const \1 = () => {\n  const { t } = useTranslation();', content)
            
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

safe_inject_i18n([
    "Dashboard.tsx", "Upload.tsx", "Login.tsx", "Register.tsx", 
    "Projects.tsx", "Results.tsx", "Profile.tsx", "Settings.tsx",
    "About.tsx", "AiAnalysis.tsx", "ColorRec.tsx", "DesignStyle.tsx", "MoodAnalysis.tsx"
])
print("Safely injected i18n")
