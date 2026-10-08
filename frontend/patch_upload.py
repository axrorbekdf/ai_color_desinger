import json
import os

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"
upload_file = "d:/Projects/ai_color_desinger/frontend/src/pages/Upload.tsx"

additions = {
    "detect_objects": {"uz": "Obyektlarni aniqlash", "en": "Detect Objects", "ru": "Определение объектов"},
    "ai_recommendations": {"uz": "AI rang tavsiyalari", "en": "AI Color Recommendations", "ru": "AI рекомендации по цвету"},
    "mood_analysis": {"uz": "Kayfiyatga moslashtirish", "en": "Mood Matching", "ru": "Подбор под настроение"},
    "upload_image": {"uz": "Rasmni yuklang", "en": "Upload Image", "ru": "Загрузить изображение"},
    "loading_project": {"uz": "Loyiha yuklanmoqda...", "en": "Loading project...", "ru": "Загрузка проекта..."},
    "project_not_found": {"uz": "Loyiha topilmadi!", "en": "Project not found!", "ru": "Проект не найден!"},
    "creating_project": {"uz": "Loyiha yaratilmoqda...", "en": "Creating project...", "ru": "Создание проекта..."},
    "uploading_image": {"uz": "Rasm yuklanmoqda...", "en": "Uploading image...", "ru": "Загрузка изображения..."},
    "detecting_objects": {"uz": "AI obyektlarni aniqlamoqda...", "en": "AI is detecting objects...", "ru": "AI определяет объекты..."},
    "error": {"uz": "Xatolik yuz berdi!", "en": "An error occurred!", "ru": "Произошла ошибка!"},
    "analyzing_colors": {"uz": "Ranglar tahlil qilinmoqda...", "en": "Analyzing colors...", "ru": "Анализ цветов..."},
    "applying_color": {"uz": "Rang qo'llanilmoqda...", "en": "Applying color...", "ru": "Применение цвета..."},
    "apply_error": {"uz": "Rang qo'llashda xatolik yuz berdi", "en": "Error applying color", "ru": "Ошибка при применении цвета"},
    "restoring": {"uz": "Asliga qaytarilmoqda...", "en": "Restoring to original...", "ru": "Восстановление оригинала..."},
    "based_on_design": {"uz": "(Dizayn va kayfiyat asosida)", "en": "(Based on design and mood)", "ru": "(На основе дизайна и настроения)"},
    "auto_select": {"uz": "Rangni avtomatik tanlash", "en": "Auto Select Color", "ru": "Автоматический выбор цвета"},
    "apply_color": {"uz": "Bu rangni qo'llash", "en": "Apply this color", "ru": "Применить этот цвет"},
    "save_palette": {"uz": "Palitrani saqlash", "en": "Save Palette", "ru": "Сохранить палитру"},
    "design_style_upload": {"uz": "Dizayn uslubi", "en": "Design Style", "ru": "Стиль дизайна"},
    "mood_upload": {"uz": "Umumiy kayfiyat", "en": "Overall Mood", "ru": "Общее настроение"},
    "color_analysis_upload": {"uz": "Rang va kayfiyat tahlili", "en": "Color and Mood Analysis", "ru": "Анализ цвета и настроения"},
    "selected_palette": {"uz": "Tanlangan rang palitrasi", "en": "Selected Color Palette", "ru": "Выбранная цветовая палитра"},
    "selected_palettes": {"uz": "Tanlangan ranglar palitrasi sizda asosan", "en": "The selected color palettes primarily reflect", "ru": "Выбранные цветовые палитры в основном отражают"},
    "positive_mood": {"uz": "ijobiy kayfiyatni", "en": "positive mood", "ru": "позитивное настроение"},
    "reflects": {"uz": "aks ettiradi. Bu palitra dam olish uchun mos.", "en": ". This palette is suitable for relaxation.", "ru": ". Эта палитра подходит для отдыха."},
    "color_meaning": {"uz": "Rang ma'nosi va psixologik ta'siri", "en": "Color Meaning and Psychological Impact", "ru": "Значение цвета и психологическое воздействие"},
    "green_desc": {"uz": "Yashil rang tabiat, tinchlik va muvozanat bilan bog'liq. U stressni kamaytiradi, ruhiy holatni yaxshilaydi va diqqatni jamlashga yordam beradi.", "en": "Green is associated with nature, peace, and balance. It reduces stress, improves mood, and helps you focus.", "ru": "Зеленый цвет ассоциируется с природой, покоем и балансом. Он снижает стресс, улучшает настроение и помогает сосредоточиться."},
    "result_upload": {"uz": "Natija (Before / After)", "en": "Result (Before / After)", "ru": "Результат (До / После)"},
    "original": {"uz": "Original", "en": "Original", "ru": "Оригинал"},
    "ai_colored": {"uz": "AI rang qo'llangan", "en": "AI Colored", "ru": "AI раскрашенный"},
    "restore": {"uz": "Asliga qaytarish", "en": "Restore Original", "ru": "Восстановить оригинал"},
    "goal_mood": {"uz": "Maqsad / Kayfiyat", "en": "Goal / Mood", "ru": "Цель / Настроение"},
    "minimalist": {"uz": "Minimalist", "en": "Minimalist", "ru": "Минимализм"},
    "calm_balanced": {"uz": "Xotirjam va muvozanatli", "en": "Calm and Balanced", "ru": "Спокойный и уравновешенный"},
    "summary": {"uz": "Xulosa", "en": "Summary", "ru": "Краткое описание"},
    "calmness": {"uz": "xotirjamlik", "en": "calmness", "ru": "спокойствие"}
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "upload" not in data:
        data["upload"] = {}
        
    for k, v in additions.items():
        data["upload"][k] = v[lang]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

with open(upload_file, "r", encoding="utf-8") as f:
    c = f.read()

replacements = {
    ">Obyektlarni aniqlash<": ">{t('upload.detect_objects')}<",
    ">AI rang tavsiyalari<": ">{t('upload.ai_recommendations')}<",
    ">Kayfiyatga moslashtirish<": ">{t('upload.mood_analysis')}<",
    "Rasmni yuklang": "{t('upload.upload_image')}",
    "'Loyiha yuklanmoqda...'": "t('upload.loading_project')",
    "'Loyiha topilmadi!'": "t('upload.project_not_found')",
    "'Loyiha yaratilmoqda...'": "t('upload.creating_project')",
    "'Rasm yuklanmoqda...'": "t('upload.uploading_image')",
    "'AI obyektlarni aniqlamoqda...'": "t('upload.detecting_objects')",
    "'Xatolik yuz berdi!'": "t('upload.error')",
    "'Ranglar tahlil qilinmoqda...'": "t('upload.analyzing_colors')",
    "\"Rang qo'llanilmoqda...\"": "t('upload.applying_color')",
    "\"Rang qo'llashda xatolik yuz berdi\"": "t('upload.apply_error')",
    "\"Asliga qaytarilmoqda...\"": "t('upload.restoring')",
    "(Dizayn va kayfiyat asosida)": "{t('upload.based_on_design')}",
    "Rangni avtomatik tanlash": "{t('upload.auto_select')}",
    "Bu rangni qo'llash": "{t('upload.apply_color')}",
    "Palitrani saqlash": "{t('upload.save_palette')}",
    ">Dizayn uslubi<": ">{t('upload.design_style_upload')}<",
    ">Umumiy kayfiyat<": ">{t('upload.mood_upload')}<",
    "Rang va kayfiyat tahlili": "{t('upload.color_analysis_upload')}",
    "Tanlangan rang palitrasi": "{t('upload.selected_palette')}",
    "Tanlangan ranglar palitrasi sizda asosan": "{t('upload.selected_palettes')}",
    "ijobiy kayfiyatni": "{t('upload.positive_mood')}",
    "aks ettiradi. Bu palitra dam olish uchun mos.": "{t('upload.reflects')}",
    "Rang ma'nosi va psixologik ta'siri": "{t('upload.color_meaning')}",
    "Yashil rang tabiat, tinchlik va muvozanat bilan bog'liq. U stressni kamaytiradi, ruhiy holatni yaxshilaydi va diqqatni jamlashga yordam beradi.": "{t('upload.green_desc')}",
    "Natija (Before / After)": "{t('upload.result_upload')}",
    ">Original<": ">{t('upload.original')}<",
    "AI rang qo'llangan": "{t('upload.ai_colored')}",
    ">Asliga qaytarish<": ">{t('upload.restore')}<",
    "Maqsad / Kayfiyat": "{t('upload.goal_mood')}",
    ">Minimalist<": ">{t('upload.minimalist')}<",
    ">Xotirjam va muvozanatli<": ">{t('upload.calm_balanced')}<",
    ">Xulosa<": ">{t('upload.summary')}<",
    ">xotirjamlik<": ">{t('upload.calmness')}<"
}

for k, v in replacements.items():
    c = c.replace(k, v)

with open(upload_file, "w", encoding="utf-8") as f:
    f.write(c)

print("Upload patched successfully")
