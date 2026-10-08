import json
import os

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"
dashboard_file = "d:/Projects/ai_color_desinger/frontend/src/pages/Dashboard.tsx"

additions = {
    "dashboard_title": {"uz": "Umumiy Statistika", "en": "Overall Statistics", "ru": "Общая статистика"},
    "dashboard_desc": {"uz": "Tizim bo'yicha barcha tahlillar xulosasi", "en": "Summary of all analyzes across the system", "ru": "Сводка всех анализов по системе"},
    "kpi_images": {"uz": "Yuklangan rasmlar", "en": "Uploaded Images", "ru": "Загруженные изображения"},
    "kpi_objects": {"uz": "Aniqlangan obyektlar", "en": "Detected Objects", "ru": "Распознанные объекты"},
    "kpi_recs": {"uz": "Berilgan tavsiyalar", "en": "Recommendations given", "ru": "Дано рекомендаций"},
    "kpi_mood": {"uz": "O'rtacha kayfiyat (ijobiy)", "en": "Avg Mood (positive)", "ru": "Среднее настроение (позитивное)"},
    "chart_title": {"uz": "Tahlil faolligi (Haftalik)", "en": "Analysis Activity (Weekly)", "ru": "Активность анализа (еженедельно)"},
    "last_7_days": {"uz": "Oxirgi 7 kun", "en": "Last 7 days", "ru": "Последние 7 дней"},
    "last_30_days": {"uz": "Oxirgi 30 kun", "en": "Last 30 days", "ru": "Последние 30 дней"},
    "popular_colors": {"uz": "Ommabop ranglar", "en": "Popular Colors", "ru": "Популярные цвета"},
    "recent_projects": {"uz": "Oxirgi loyihalar", "en": "Recent Projects", "ru": "Последние проекты"},
    "see_all": {"uz": "Barchasini ko'rish", "en": "See all", "ru": "Смотреть все"},
    "file_name": {"uz": "Fayl nomi", "en": "File Name", "ru": "Имя файла"},
    "date": {"uz": "Sana", "en": "Date", "ru": "Дата"},
    "obj_count": {"uz": "Obyektlar soni", "en": "Object count", "ru": "Кол-во объектов"},
    "status": {"uz": "Holat", "en": "Status", "ru": "Статус"},
    "no_projects_dash": {"uz": "Hali loyihalar mavjud emas. Yangi rasm yuklang!", "en": "No projects yet. Upload a new image!", "ru": "Пока нет проектов. Загрузите новое изображение!"},
    "new_project_btn": {"uz": "Yangi loyiha", "en": "New project", "ru": "Новый проект"},
    "color_red": {"uz": "Qizil", "en": "Red", "ru": "Красный"},
    "color_blue": {"uz": "Ko'k", "en": "Blue", "ru": "Синий"},
    "color_green": {"uz": "Yashil", "en": "Green", "ru": "Зеленый"},
    "color_yellow": {"uz": "Sariq", "en": "Yellow", "ru": "Желтый"},
    "color_purple": {"uz": "Binafsha", "en": "Purple", "ru": "Фиолетовый"}
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "dashboard" not in data:
        data["dashboard"] = {}
        
    for k, v in additions.items():
        data["dashboard"][k] = v[lang]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

with open(dashboard_file, "r", encoding="utf-8") as f:
    c = f.read()

replacements = {
    ">Umumiy Statistika<": ">{t('dashboard.dashboard_title')}<",
    ">Tizim bo'yicha barcha tahlillar xulosasi<": ">{t('dashboard.dashboard_desc')}<",
    ">Yuklangan rasmlar<": ">{t('dashboard.kpi_images')}<",
    "name=\"Yuklangan rasmlar\"": "name={t('dashboard.kpi_images')}",
    ">Aniqlangan obyektlar<": ">{t('dashboard.kpi_objects')}<",
    ">Berilgan tavsiyalar<": ">{t('dashboard.kpi_recs')}<",
    ">O'rtacha kayfiyat (iijobiy)<": ">{t('dashboard.kpi_mood')}<",
    ">Tahlil faolligi (Haftalik)<": ">{t('dashboard.chart_title')}<",
    ">Oxirgi 7 kun<": ">{t('dashboard.last_7_days')}<",
    ">Oxirgi 30 kun<": ">{t('dashboard.last_30_days')}<",
    ">Ommabop ranglar<": ">{t('dashboard.popular_colors')}<",
    ">Oxirgi loyihalar<": ">{t('dashboard.recent_projects')}<",
    ">Fayl nomi<": ">{t('dashboard.file_name')}<",
    ">Sana<": ">{t('dashboard.date')}<",
    ">Obyektlar soni<": ">{t('dashboard.obj_count')}<",
    ">Holat<": ">{t('dashboard.status')}<",
    ">Hali loyihalar mavjud emas. Yangi rasm yuklang!<": ">{t('dashboard.no_projects_dash')}<",
    ">Yangi loyiha<": ">{t('dashboard.new_project_btn')}<",
    "'Qizil'": "t('dashboard.color_red')",
    "'Ko\\'k'": "t('dashboard.color_blue')",
    "'Yashil'": "t('dashboard.color_green')",
    "'Sariq'": "t('dashboard.color_yellow')",
    "'Binafsha'": "t('dashboard.color_purple')"
}

for k, v in replacements.items():
    c = c.replace(k, v)

with open(dashboard_file, "w", encoding="utf-8") as f:
    f.write(c)

print("Dashboard patched successfully")
