import os
import json

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"

additions = {
    "sidebar": {
        "about": {"uz": "Biz haqimizda", "en": "About Us", "ru": "О нас"}
    },
    "results_empty_desc": {"uz": "Rasmlarni yuklang va obyektlarning rangini o'zgartiring. Barcha qilingan amallar shu yerda saqlanib boradi.", "en": "Upload images and change object colors. All performed actions will be saved here.", "ru": "Загрузите изображения и измените цвета объектов. Все выполненные действия будут сохранены здесь."},
    "open_project": {"uz": "Loyihani ochish", "en": "Open Project", "ru": "Открыть проект"},
    "open": {"uz": "Ochish", "en": "Open", "ru": "Открыть"},
    "project_name": {"uz": "Loyiha nomi", "en": "Project Name", "ru": "Название проекта"},
    "result": {"uz": "Natija", "en": "Result", "ru": "Результат"},
    "color_changed": {"uz": "Rang o'zgartirildi", "en": "Color changed", "ru": "Цвет изменен"}
}

def update_locales():
    for lang in ["uz", "en", "ru"]:
        file_path = os.path.join(locales_dir, lang, "translation.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Add to sidebar
        if "about" not in data["sidebar"]:
            data["sidebar"]["about"] = additions["sidebar"]["about"][lang]
            
        for k, v in additions.items():
            if k != "sidebar":
                data[k] = v[lang]
            
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

update_locales()
print("Locales updated with new Results keys")

# Now patch Results.tsx
base_dir = "d:/Projects/ai_color_desinger/frontend/src/pages"
results_file = os.path.join(base_dir, "Results.tsx")

with open(results_file, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "Rasmlarni yuklang va obyektlarning rangini o'zgartiring. Barcha qilingan amallar shu yerda saqlanib boradi.": "{t('results_empty_desc')}",
    "Boshlash": "{t('start')}",
    "Loyihani ochish": "{t('open_project')}",
    "Loyiha nomi:": "{t('project_name')}:",
    "Natija": "{t('result')}",
    "Rang o'zgartirildi": "{t('color_changed')}",
    "Ochish": "{t('open')}"
}

for k, v in replacements.items():
    content = content.replace(k, v)

# wait, "Boshlash <ArrowRight" -> "{t('start')} <ArrowRight"
# "Natija\n" will be "{t('result')}\n"
# Actually direct string replacement works perfectly.

with open(results_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Results patched")
