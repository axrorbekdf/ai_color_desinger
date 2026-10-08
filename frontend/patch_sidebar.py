import json
import os

locales = {
    "uz": {
        "sidebar": {
            "aiAnalysis": "AI tahlili",
            "colorRec": "Rang tavsiyasi",
            "moodAnalysis": "Kayfiyat tahlili",
            "designStyle": "Dizayn uslubi",
            "results": "Natijalar",
            "tip": "Maslahat",
            "tipText": "Rang nafaqat dizaynni, balki kayfiyatingizni ham o'zgartirishi mumkin.",
            "about": "Biz haqimizda"
        },
        "header": {
            "user": "Foydalanuvchi"
        }
    },
    "en": {
        "sidebar": {
            "aiAnalysis": "AI Analysis",
            "colorRec": "Color Recommendation",
            "moodAnalysis": "Mood Analysis",
            "designStyle": "Design Style",
            "results": "Results",
            "tip": "Tip",
            "tipText": "Color can change not only the design but also your mood.",
            "about": "About Us"
        },
        "header": {
            "user": "User"
        }
    },
    "ru": {
        "sidebar": {
            "aiAnalysis": "ИИ анализ",
            "colorRec": "Рекомендации по цвету",
            "moodAnalysis": "Анализ настроения",
            "designStyle": "Стиль дизайна",
            "results": "Результаты",
            "tip": "Совет",
            "tipText": "Цвет может изменить не только дизайн, но и ваше настроение.",
            "about": "О нас"
        },
        "header": {
            "user": "Пользователь"
        }
    }
}

base_dir = r"d:\Projects\ai_color_desinger\frontend\src\locales"

for lang, data in locales.items():
    path = os.path.join(base_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    if "sidebar" not in existing:
        existing["sidebar"] = {}
    existing["sidebar"].update(data["sidebar"])
    
    if "header" not in existing:
        existing["header"] = {}
    existing["header"].update(data["header"])
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

print("Added sidebar and header keys")
