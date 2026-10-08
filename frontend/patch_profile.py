import os
import json

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"
profile_file = "d:/Projects/ai_color_desinger/frontend/src/pages/Profile.tsx"

additions = {
    "profile_title": {"uz": "Mening profilim", "en": "My Profile", "ru": "Мой профиль"},
    "profile_desc": {"uz": "Shaxsiy ma'lumotlar va xavfsizlik sozlamalari", "en": "Personal information and security settings", "ru": "Личная информация и настройки безопасности"},
    "active_user": {"uz": "Faol foydalanuvchi", "en": "Active User", "ru": "Активный пользователь"},
    "logout": {"uz": "Tizimdan chiqish", "en": "Logout", "ru": "Выйти"},
    "change_password": {"uz": "Parolni o'zgartirish", "en": "Change Password", "ru": "Изменить пароль"},
    "current_password": {"uz": "Joriy parol", "en": "Current Password", "ru": "Текущий пароль"},
    "new_password": {"uz": "Yangi parol", "en": "New Password", "ru": "Новый пароль"},
    "save": {"uz": "Saqlash", "en": "Save", "ru": "Сохранить"},
    "saved_success": {"uz": "Muvaffaqiyatli saqlandi", "en": "Saved successfully", "ru": "Успешно сохранено"}
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "profile" not in data:
        data["profile"] = {}
        
    for k, v in additions.items():
        data["profile"][k] = v[lang]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

with open(profile_file, "r", encoding="utf-8") as f:
    c = f.read()

replacements = {
    ">Mening profilim<": ">{t('profile.profile_title')}<",
    ">Shaxsiy ma'lumotlar va xavfsizlik sozlamalari<": ">{t('profile.profile_desc')}<",
    ">Foydalanuvchi<": ">{t('header.user')}<",
    "Faol foydalanuvchi": "{t('profile.active_user')}",
    "Tizimdan chiqish": "{t('profile.logout')}",
    "Parolni o'zgartirish": "{t('profile.change_password')}",
    "Joriy parol": "{t('profile.current_password')}",
    "Yangi parol": "{t('profile.new_password')}",
    ">Saqlash<": ">{t('profile.save')}<",
    "Muvaffaqiyatli saqlandi": "{t('profile.saved_success')}"
}

for k, v in replacements.items():
    c = c.replace(k, v)

with open(profile_file, "w", encoding="utf-8") as f:
    f.write(c)

print("Profile patched successfully")
