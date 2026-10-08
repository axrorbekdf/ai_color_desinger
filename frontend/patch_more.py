import os
import re
import json

base_dir = "d:/Projects/ai_color_desinger/frontend/src/pages"
locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"

translations = {
    "profile_title": {"uz": "Mening profilim", "en": "My Profile", "ru": "Мой профиль"},
    "profile_desc": {"uz": "Shaxsiy ma'lumotlar va xavfsizlik sozlamalari", "en": "Personal information and security settings", "ru": "Личная информация и настройки безопасности"},
    "active_user": {"uz": "Faol foydalanuvchi", "en": "Active user", "ru": "Активный пользователь"},
    "logout": {"uz": "Tizimdan chiqish", "en": "Logout", "ru": "Выйти"},
    "change_password": {"uz": "Parolni o'zgartirish", "en": "Change Password", "ru": "Изменить пароль"},
    "current_password": {"uz": "Joriy parol", "en": "Current Password", "ru": "Текущий пароль"},
    "new_password": {"uz": "Yangi parol", "en": "New Password", "ru": "Новый пароль"},
    
    "results_title": {"uz": "Barcha natijalar", "en": "All Results", "ru": "Все результаты"},
    "results_desc": {"uz": "Ranglar ustida olib borilgan amallar tarixi", "en": "History of color operations", "ru": "История операций с цветами"},
    "no_results": {"uz": "Hali natijalar yo'q", "en": "No results yet", "ru": "Пока нет результатов"},
    "no_results_desc": {"uz": "Birinchi marta loyiha yaratib, ranglarni o'zgartirganingizda, natijalar shu yerda paydo bo'ladi.", "en": "When you create a project and change colors, results will appear here.", "ru": "Когда вы создадите проект и измените цвета, результаты появятся здесь."},
    "changed": {"uz": "O'zgartirildi", "en": "Changed", "ru": "Изменено"},
    "applied_color": {"uz": "Qo'llanilgan rang:", "en": "Applied color:", "ru": "Примененный цвет:"}
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

def replace_in_file(filename, replacements):
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "useTranslation" not in content:
        content = content.replace("import React", "import React\nimport { useTranslation } from 'react-i18next';")
        content = re.sub(r'export const (\w+) = \(\) => {', r'export const \1 = () => {\n  const { t } = useTranslation();', content)
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

profile_rep = {
    "Mening profilim": "{t('profile_title')}",
    "Shaxsiy ma'lumotlar va xavfsizlik sozlamalari": "{t('profile_desc')}",
    "Faol foydalanuvchi": "{t('active_user')}",
    "Tizimdan chiqish": "{t('logout')}",
    "Parolni o'zgartirish": "{t('change_password')}",
    "Joriy parol": "{t('current_password')}",
    "Yangi parol": "{t('new_password')}"
}
replace_in_file("Profile.tsx", profile_rep)

results_rep = {
    "Barcha natijalar": "{t('results_title')}",
    "Ranglar ustida olib borilgan amallar tarixi": "{t('results_desc')}",
    "Hali natijalar yo'q": "{t('no_results')}",
    "Birinchi marta loyiha yaratib, ranglarni o'zgartirganingizda, natijalar shu yerda paydo bo'ladi.": "{t('no_results_desc')}",
    "O'zgartirildi": "{t('changed')}",
    "Qo'llanilgan rang:": "{t('applied_color')}:"
}
replace_in_file("Results.tsx", results_rep)

print("More files patched.")
