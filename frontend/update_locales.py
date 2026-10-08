import os
import json

base_dir = "d:/Projects/ai_color_desinger/frontend/src"
locales_dir = os.path.join(base_dir, "locales")

translations = {
    "upload_title": {"uz": "Rasm yuklash", "en": "Upload Image", "ru": "Загрузить изображение"},
    "drag_drop": {"uz": "Yangi rasm yuklash yoki tashlash", "en": "Upload or drag & drop new image", "ru": "Загрузите или перетащите новое изображение"},
    "analyzing": {"uz": "Tahlil qilinmoqda...", "en": "Analyzing...", "ru": "Анализ..."},
    "please_wait": {"uz": "Kutib turing...", "en": "Please wait...", "ru": "Подождите..."},
    "tab_detect": {"uz": "Obyektni tahlil qilish", "en": "Detect Objects", "ru": "Определение объектов"},
    "tab_color": {"uz": "Rang tanlash", "en": "Color Selection", "ru": "Выбор цвета"},
    "tab_result": {"uz": "Natija", "en": "Result", "ru": "Результат"},
    "reset": {"uz": "Asliga qaytarish", "en": "Reset to Original", "ru": "Сбросить к оригиналу"},
    "save": {"uz": "Saqlash", "en": "Save", "ru": "Сохранить"},
    "recommended_colors": {"uz": "Tavsiya etilgan ranglar", "en": "Recommended Colors", "ru": "Рекомендуемые цвета"},
    "compatibility": {"uz": "Moslik", "en": "Match", "ru": "Совместимость"},
    "select": {"uz": "Tanlash", "en": "Select", "ru": "Выбрать"},
    "no_projects": {"uz": "Hali loyihalar yo'q", "en": "No projects yet", "ru": "Пока нет проектов"},
    "first_upload_tip": {"uz": "Birinchi rasmingizni yuklang, tizim uni avtomatik alohida loyiha sifatida saqlab qoladi.", "en": "Upload your first image, the system will automatically save it as a separate project.", "ru": "Загрузите свое первое изображение, система автоматически сохранит его как отдельный проект."},
    "start": {"uz": "Boshlash", "en": "Start", "ru": "Начать"},
    "edited": {"uz": "Tahrirlangan", "en": "Edited", "ru": "Отредактировано"},
    "objects_detected": {"uz": "obyekt aniqlangan", "en": "objects detected", "ru": "объектов найдено"},
    "delete_confirm": {"uz": "O'chirishni tasdiqlaysizmi?", "en": "Confirm deletion?", "ru": "Подтвердите удаление?"},
    "delete_warning": {"uz": "Bu loyiha va uning barcha amallar tarixi butunlay o'chib ketadi. Buni ortga qaytarib bo'lmaydi.", "en": "This project and all its history will be permanently deleted. This cannot be undone.", "ru": "Этот проект и вся его история будут безвозвратно удалены. Это действие нельзя отменить."},
    "cancel": {"uz": "Bekor qilish", "en": "Cancel", "ru": "Отмена"},
    "delete": {"uz": "O'chirish", "en": "Delete", "ru": "Удалить"},
    "dashboard_stats": {"uz": "Statistika", "en": "Statistics", "ru": "Статистика"},
    "total_projects": {"uz": "Jami loyihalar", "en": "Total Projects", "ru": "Всего проектов"},
    "objects_found": {"uz": "Obyektlar aniqlandi", "en": "Objects Found", "ru": "Объектов найдено"},
    "recent_activity": {"uz": "So'nggi faollik", "en": "Recent Activity", "ru": "Последняя активность"},
    "my_projects_desc": {"uz": "Barcha yuklangan va tahrirlangan rasmlar tarixi", "en": "History of all uploaded and edited images", "ru": "История всех загруженных и отредактированных изображений"},
    "new_upload": {"uz": "Yangi rasm yuklash", "en": "Upload New Image", "ru": "Загрузить новое изображение"}
}

def update_locales():
    for lang in ["uz", "en", "ru"]:
        file_path = os.path.join(locales_dir, lang, "translation.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for key, vals in translations.items():
            data[key] = vals[lang]
            
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

update_locales()
print("Locales updated.")
