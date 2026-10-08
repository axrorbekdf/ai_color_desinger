import os
import json

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"
projects_file = "d:/Projects/ai_color_desinger/frontend/src/pages/Projects.tsx"

additions = {
    "projects_title": {"uz": "Loyihalarim", "en": "My Projects", "ru": "Мои проекты"},
    "projects_desc": {"uz": "Barcha yuklangan va tahrirlangan rasmlar tarixi", "en": "History of all uploaded and edited images", "ru": "История всех загруженных и отредактированных изображений"},
    "new_image_upload": {"uz": "Yangi rasm yuklash", "en": "Upload new image", "ru": "Загрузить новое изображение"},
    "no_projects": {"uz": "Hali loyihalar yo'q", "en": "No projects yet", "ru": "Пока нет проектов"},
    "no_projects_desc": {"uz": "Birinchi rasmingizni yuklang, tizim uni avtomatik alohida loyiha sifatida saqlab qoladi.", "en": "Upload your first image, the system will automatically save it as a separate project.", "ru": "Загрузите свое первое изображение, система автоматически сохранит его как отдельный проект."},
    "start_btn": {"uz": "Boshlash", "en": "Start", "ru": "Начать"},
    "new_project": {"uz": "Yangi Loyiha", "en": "New Project", "ru": "Новый проект"},
    "edited_badge": {"uz": "Tahrirlangan", "en": "Edited", "ru": "Изменено"},
    "objects_found": {"uz": "obyekt aniqlangan", "en": "objects found", "ru": "объектов найдено"},
    "objects_short": {"uz": "obyekt", "en": "objects", "ru": "объектов"},
    "delete_title": {"uz": "O'chirishni tasdiqlash", "en": "Confirm Delete", "ru": "Подтвердить удаление"},
    "delete_desc": {"uz": "Rostdan ham bu loyihani o'chirib tashlamoqchimisiz? Bu amalni orqaga qaytarib bo'lmaydi.", "en": "Are you sure you want to delete this project? This action cannot be undone.", "ru": "Вы уверены, что хотите удалить этот проект? Это действие нельзя отменить."},
    "cancel": {"uz": "Bekor qilish", "en": "Cancel", "ru": "Отмена"},
    "delete": {"uz": "O'chirish", "en": "Delete", "ru": "Удалить"}
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for k, v in additions.items():
        data[k] = v[lang]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

with open(projects_file, "r", encoding="utf-8") as f:
    c = f.read()

replacements = {
    ">Loyihalarim<": ">{t('projects_title')}<",
    ">Barcha yuklangan va tahrirlangan rasmlar tarixi<": ">{t('projects_desc')}<",
    "Yangi rasm yuklash": "{t('new_image_upload')}",
    ">Hali loyihalar yo'q<": ">{t('no_projects')}<",
    "Birinchi rasmingizni yuklang, tizim uni avtomatik alohida loyiha sifatida saqlab qoladi.": "{t('no_projects_desc')}",
    "Boshlash <ArrowRight": "{t('start_btn')} <ArrowRight",
    "'Yangi Loyiha'": "t('new_project')",
    ">Tahrirlangan<": ">{t('edited_badge')}<",
    "} obyekt aniqlangan": "} {t('objects_found')}",
    "} obyekt<": "} {t('objects_short')}<",
    ">O'chirishni tasdiqlash<": ">{t('delete_title')}<",
    ">Rostdan ham bu loyihani o'chirib tashlamoqchimisiz? Bu amalni orqaga qaytarib bo'lmaydi.<": ">{t('delete_desc')}<",
    ">Bekor qilish<": ">{t('cancel')}<",
    ">O'chirish<": ">{t('delete')}<"
}

for k, v in replacements.items():
    c = c.replace(k, v)

with open(projects_file, "w", encoding="utf-8") as f:
    f.write(c)

print("Projects patched successfully")
