import json
import os

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"
login_file = "d:/Projects/ai_color_desinger/frontend/src/pages/Login.tsx"
register_file = "d:/Projects/ai_color_desinger/frontend/src/pages/Register.tsx"

additions = {
    "login_title": {"uz": "Tizimga kirish", "en": "Sign In", "ru": "Вход в систему"},
    "email": {"uz": "Email", "en": "Email", "ru": "Email"},
    "password": {"uz": "Parol", "en": "Password", "ru": "Пароль"},
    "login_btn": {"uz": "Kirish", "en": "Sign In", "ru": "Войти"},
    "no_account": {"uz": "Akkauntingiz yo'qmi?", "en": "Don't have an account?", "ru": "Нет аккаунта?"},
    "register_link": {"uz": "Ro'yxatdan o'tish", "en": "Sign Up", "ru": "Зарегистрироваться"},
    "register_title": {"uz": "Ro'yxatdan o'tish", "en": "Sign Up", "ru": "Регистрация"},
    "name": {"uz": "Ism", "en": "Name", "ru": "Имя"},
    "has_account": {"uz": "Akkauntingiz bormi?", "en": "Already have an account?", "ru": "Уже есть аккаунт?"}
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "auth" not in data:
        data["auth"] = {}
        
    for k, v in additions.items():
        data["auth"][k] = v[lang]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


with open(login_file, "r", encoding="utf-8") as f:
    c = f.read()

replacements = {
    ">Tizimga kirish<": ">{t('auth.login_title')}<",
    ">Email<": ">{t('auth.email')}<",
    ">Parol<": ">{t('auth.password')}<",
    ">Kirish<": ">{t('auth.login_btn')}<",
    "Akkauntingiz yo'qmi?": "{t('auth.no_account')}",
    "Ro'yxatdan o'tish": "{t('auth.register_link')}"
}

for k, v in replacements.items():
    c = c.replace(k, v)

with open(login_file, "w", encoding="utf-8") as f:
    f.write(c)


with open(register_file, "r", encoding="utf-8") as f:
    c = f.read()

replacements_reg = {
    ">Ro'yxatdan o'tish<": ">{t('auth.register_title')}<",
    ">Ism<": ">{t('auth.name')}<",
    ">Email<": ">{t('auth.email')}<",
    ">Parol<": ">{t('auth.password')}<",
    "Akkauntingiz bormi?": "{t('auth.has_account')}",
    "Kirish": "{t('auth.login_btn')}"
}

for k, v in replacements_reg.items():
    c = c.replace(k, v)

with open(register_file, "w", encoding="utf-8") as f:
    f.write(c)

print("Auth patched successfully")
