import json
import os

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"

additions = {
    "results_title": {"uz": "Amallar tarixi", "en": "Action History", "ru": "История действий"},
    "results_desc": {"uz": "Loyihalar ustida qilingan barcha rang o'zgartirish amallari", "en": "All color change actions performed on projects", "ru": "Все действия по изменению цвета, выполненные в проектах"},
    "header": {
        "user": {"uz": "Foydalanuvchi", "en": "User", "ru": "Пользователь"}
    }
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "sidebar" not in data:
        data["sidebar"] = {}
    if "dashboard" not in data["sidebar"]:
        data["sidebar"]["dashboard"] = {"uz": "Bosh sahifa", "en": "Dashboard", "ru": "Главная"}[lang]
    
    if "header" not in data:
        data["header"] = {}
    data["header"]["user"] = additions["header"]["user"][lang]
    
    data["results_title"] = additions["results_title"][lang]
    data["results_desc"] = additions["results_desc"][lang]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated translations")
