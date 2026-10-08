import os

filepath = r"d:\Projects\ai_color_desinger\frontend\src\pages\Upload.tsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add useToastStore import
content = content.replace("import api from '../services/api';", "import api from '../services/api';\nimport { useToastStore } from '../store/useToastStore';")

# Add addToast hook
content = content.replace("const { t } = useTranslation();", "const { t } = useTranslation();\n  const { addToast } = useToastStore();")

# Replace alerts
content = content.replace("alert('Xatolik yuz berdi!');", "addToast('Xatolik yuz berdi!', 'error');")
content = content.replace("alert(\"Rang qo'llashda xatolik yuz berdi\");", "addToast(\"Rang qo'llashda xatolik yuz berdi\", 'error');")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed Upload alerts")
