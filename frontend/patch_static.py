import os
import json
import re

base_dir = "d:/Projects/ai_color_desinger/frontend/src/pages"
locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"

translations = {
    # About
    "about_title": {"uz": "Sun'iy intellekt yordamida interyer dizaynini yaratish", "en": "Creating interior design using Artificial Intelligence", "ru": "Создание дизайна интерьера с помощью ИИ"},
    "about_subtitle": {"uz": "Ushbu loyiha zamonaviy AI texnologiyalaridan foydalanib, rasmlardagi obyektlarni aniqlash va ularga mos ranglar palitrasini tavsiya etish imkonini beradi.", "en": "This project uses modern AI technologies to detect objects in images and recommend matching color palettes.", "ru": "Этот проект использует современные технологии ИИ для обнаружения объектов на изображениях и рекомендации подходящих цветовых палитр."},
    "about_goal": {"uz": "Loyiha maqsadi", "en": "Project Goal", "ru": "Цель проекта"},
    "about_thesis": {"uz": "Magistrlik dissertatsiyasi", "en": "Master's Thesis", "ru": "Магистерская диссертация"},
    "about_desc": {"uz": "AI Color Designer dasturi interyer dizaynerlari, arxitektorlar va oddiy foydalanuvchilarga xona dizaynini yaratishda yordam berish uchun ishlab chiqilgan. Dastur insonning psixologik holatiga ijobiy ta'sir ko'rsatadigan ranglarni tanlash va ularni to'g'ridan-to'g'ri rasmdagi jihozlarga qo'llash imkoniyatini taqdim etadi.", "en": "AI Color Designer is designed to help interior designers, architects, and regular users create room designs. The program provides the ability to select colors that positively affect a person's psychological state and apply them directly to the furniture in the image.", "ru": "AI Color Designer разработан, чтобы помочь дизайнерам интерьера, архитекторам и обычным пользователям создавать дизайн комнат. Программа предоставляет возможность выбирать цвета, которые положительно влияют на психологическое состояние человека, и применять их непосредственно к мебели на изображении."},
    "about_tech": {"uz": "Texnologiyalar", "en": "Technologies", "ru": "Технологии"},
    "about_stack": {"uz": "Stek va asboblar", "en": "Stack and Tools", "ru": "Стек и инструменты"},
    "about_feat1": {"uz": "Avtomatik obyektlarni aniqlash (Mask R-CNN)", "en": "Automatic object detection (Mask R-CNN)", "ru": "Автоматическое обнаружение объектов (Mask R-CNN)"},
    "about_feat2": {"uz": "Ranglarning psixologik tahlili", "en": "Psychological analysis of colors", "ru": "Психологический анализ цветов"},
    "about_feat3": {"uz": "Mos keluvchi ranglar palitrasini tavsiya etish", "en": "Recommending matching color palettes", "ru": "Рекомендация подходящих цветовых палитр"},
    "about_feat4": {"uz": "Tanlangan rangni rasmga real-vaqtda qo'llash", "en": "Applying the selected color to the image in real-time", "ru": "Применение выбранного цвета к изображению в реальном времени"},
    "about_extra": {"uz": "Qo'shimcha", "en": "Additional", "ru": "Дополнительно"},

    # AiAnalysis
    "ai_title": {"uz": "Sun'iy intellekt tahlili", "en": "Artificial Intelligence Analysis", "ru": "Анализ искусственного интеллекта"},
    "ai_desc": {"uz": "Mask R-CNN algoritmi yordamida rasmlardagi mebel va xona elementlarini avtomatik aniqlash jarayoni.", "en": "The process of automatically detecting furniture and room elements in images using the Mask R-CNN algorithm.", "ru": "Процесс автоматического обнаружения мебели и элементов комнаты на изображениях с помощью алгоритма Mask R-CNN."},
    "ai_scan": {"uz": "Tasvirni skanerlash", "en": "Image Scanning", "ru": "Сканирование изображения"},
    "ai_scan_desc": {"uz": "Yuklangan rasm piksellar kesimida tahlil qilinadi va chuqur neyron tarmoqlar yordamida xususiyatlar ajratib olinadi.", "en": "The uploaded image is analyzed at the pixel level and features are extracted using deep neural networks.", "ru": "Загруженное изображение анализируется на уровне пикселей, и с помощью глубоких нейронных сетей извлекаются признаки."},
    "ai_seg": {"uz": "Obyektlarni ajratish", "en": "Object Segmentation", "ru": "Сегментация объектов"},
    "ai_seg_desc": {"uz": "Devor, poydevor, stol, divan kabi obyektlarning aniq chegaralari belgilanadi (Bounding Box va Segmentation Mask).", "en": "Accurate boundaries of objects such as walls, floors, tables, and sofas are defined (Bounding Box and Segmentation Mask).", "ru": "Определяются точные границы объектов, таких как стены, полы, столы и диваны (Bounding Box и Segmentation Mask)."},
    "ai_layer": {"uz": "Qatlamli tahlil", "en": "Layer Analysis", "ru": "Послойный анализ"},
    "ai_layer_desc": {"uz": "Har bir topilgan obyekt alohida qatlam sifatida saqlanib, keyinchalik faqat o'sha qismni bo'yash imkonini beradi.", "en": "Each detected object is saved as a separate layer, allowing only that part to be painted later.", "ru": "Каждый обнаруженный объект сохраняется как отдельный слой, что позволяет позже раскрасить только эту часть."},
    "ai_try": {"uz": "O'z rasmingizni tahlil qilib ko'rasizmi?", "en": "Want to analyze your own image?", "ru": "Хотите проанализировать свое изображение?"},
    "ai_try_desc": {"uz": "Dasturimiz hozirda 80 dan ortiq uy jihozlari va arxitektura elementlarini taniy oladi. Hoziroq sinab ko'ring.", "en": "Our software can currently recognize over 80 home furnishings and architectural elements. Try it now.", "ru": "Наше программное обеспечение в настоящее время может распознавать более 80 предметов домашней обстановки и архитектурных элементов. Попробуйте прямо сейчас."},
    "ai_start": {"uz": "Tahlilni boshlash", "en": "Start Analysis", "ru": "Начать анализ"},

    # ColorRec
    "color_title": {"uz": "Aqliy rang tavsiyalari", "en": "Smart Color Recommendations", "ru": "Умные цветовые рекомендации"},
    "color_desc": {"uz": "Xonaning yorug'ligi, uslubi va maqsadiga qarab mukammal ranglar uyg'unligini yarating.", "en": "Create the perfect color harmony depending on the room's lighting, style, and purpose.", "ru": "Создайте идеальную цветовую гармонию в зависимости от освещения, стиля и назначения комнаты."},
    "color_pop": {"uz": "Ommabop palitralar", "en": "Popular Palettes", "ru": "Популярные палитры"},
    "color_p1": {"uz": "Sokin Dengiz", "en": "Calm Sea", "ru": "Спокойное море"},
    "color_p2": {"uz": "Kuzgi Barglar", "en": "Autumn Leaves", "ru": "Осенние листья"},
    "color_p3": {"uz": "Minimalist Oq", "en": "Minimalist White", "ru": "Минималистичный белый"},
    "color_p4": {"uz": "Bahor Tongi", "en": "Spring Morning", "ru": "Весеннее утро"},
    "color_light": {"uz": "Yorug'lik harorati", "en": "Light Temperature", "ru": "Температура света"},
    "color_light_desc": {"uz": "Issiq yorug'lik xonaga shinamlik bersa, sovuq yorug'lik rasmiylik va kenglik tasavvurini uyg'otadi. Dastur buni hisobga olib rang taklif qiladi.", "en": "Warm lighting gives a room a cozy feel, while cool lighting evokes formality and spaciousness. The program considers this when suggesting colors.", "ru": "Теплое освещение придает комнате уют, а холодное - ощущение формальности и простора. Программа учитывает это при предложении цветов."},
    "color_rule": {"uz": "60-30-10 Qoidasi", "en": "60-30-10 Rule", "ru": "Правило 60-30-10"},
    "color_rule_desc": {"uz": "60% asosiy rang (devorlar), 30% ikkilamchi rang (mebellar), 10% urg'u beruvchi rang (dekoratsiyalar). Bu oltin qoida dizaynni boyitadi.", "en": "60% dominant color (walls), 30% secondary color (furniture), 10% accent color (decorations). This golden rule enriches the design.", "ru": "60% доминирующий цвет (стены), 30% вторичный цвет (мебель), 10% акцентный цвет (декорации). Это золотое правило обогащает дизайн."},
    "color_try": {"uz": "Xonangizga mos rang tanlaymizmi?", "en": "Shall we choose a color for your room?", "ru": "Выберем цвет для вашей комнаты?"},
    "color_try_desc": {"uz": "Rasmingizni yuklang, AI unga mos ranglarni avtomatik tavsiya qiladi.", "en": "Upload your image, AI will automatically recommend matching colors.", "ru": "Загрузите изображение, ИИ автоматически порекомендует подходящие цвета."},
    "color_btn": {"uz": "Rang tanlash", "en": "Choose Color", "ru": "Выбрать цвет"},

    # MoodAnalysis
    "mood_title": {"uz": "Kayfiyat tahlili", "en": "Mood Analysis", "ru": "Анализ настроения"},
    "mood_desc": {"uz": "Ranglar bizning his-tuyg'ularimiz va psixologiyamizga qanday ta'sir qilishini bilib oling.", "en": "Find out how colors affect our emotions and psychology.", "ru": "Узнайте, как цвета влияют на наши эмоции и психологию."},
    "mood_m1": {"uz": "Xotirjamlik", "en": "Calmness", "ru": "Спокойствие"},
    "mood_m1_desc": {"uz": "Ko'k va havorang ohanglar stressni kamaytiradi, diqqatni jamlashga yordam beradi. Yotoqxona uchun mos.", "en": "Blue and light blue tones reduce stress and help focus. Suitable for the bedroom.", "ru": "Синие и голубые тона снижают стресс и помогают сосредоточиться. Подходит для спальни."},
    "mood_m2": {"uz": "G'ayrat va Energiya", "en": "Vigor and Energy", "ru": "Бодрость и энергия"},
    "mood_m2_desc": {"uz": "Qizil va zarg'aldoq ranglar ishtahani ochadi va harakatga undaydi. Oshxona va sport xonalariga xos.", "en": "Red and orange colors stimulate appetite and encourage action. Typical for kitchens and sports rooms.", "ru": "Красный и оранжевый цвета стимулируют аппетит и побуждают к действию. Характерно для кухонь и спортивных комнат."},
    "mood_m3": {"uz": "Issiqlik va Shinamlik", "en": "Warmth and Coziness", "ru": "Тепло и уют"},
    "mood_m3_desc": {"uz": "Sariq, jigarrang kabi tuproq ranglari insonga qulaylik hissini beradi. Mehmonxonalar uchun ideal.", "en": "Earth colors like yellow and brown give people a sense of comfort. Ideal for living rooms.", "ru": "Земляные цвета, такие как желтый и коричневый, придают людям чувство комфорта. Идеально для гостиных."},
    "mood_m4": {"uz": "Ijobiylik va Ijodkorlik", "en": "Positivity and Creativity", "ru": "Позитив и творчество"},
    "mood_m4_desc": {"uz": "Siyohrang va yashil ranglar tasavvurni kengaytirib, miya faoliyatini yaxshilaydi. Ish xonalariga mos.", "en": "Purple and green colors expand imagination and improve brain function. Suitable for workrooms.", "ru": "Фиолетовый и зеленый цвета расширяют воображение и улучшают работу мозга. Подходит для рабочих комнат."},
    "mood_try": {"uz": "Sizning uyingiz qanday kayfiyat beradi?", "en": "What mood does your home give?", "ru": "Какое настроение создает ваш дом?"},
    "mood_try_desc": {"uz": "O'z rasmingizni tizimga yuklang va maqsadli kayfiyatni tanlab, AI yordamida dizayn yarating.", "en": "Upload your image to the system, choose a target mood, and create a design using AI.", "ru": "Загрузите свое изображение в систему, выберите целевое настроение и создайте дизайн с помощью ИИ."},
    
    # DesignStyle
    "ds_title": {"uz": "Dizayn uslubi", "en": "Design Style", "ru": "Стиль дизайна"},
    "ds_desc": {"uz": "Arxitektura va interyer dizayn uslublari bilan tanishing hamda o'z uyingizni shu yo'nalishlarda bezating.", "en": "Get acquainted with architectural and interior design styles and decorate your home in these directions.", "ru": "Познакомьтесь с архитектурными и интерьерными стилями дизайна и украсьте свой дом в этих направлениях."},
    "ds_s1": {"uz": "Modern (Zamonaviy)", "en": "Modern", "ru": "Модерн (Современный)"},
    "ds_s1_desc": {"uz": "Toza chiziqlar, minimalist yondashuv va asosan oq-qora, neytral ranglar palitrasi. Shisha, metall va beton ko'p ishlatiladi.", "en": "Clean lines, minimalist approach, and mostly black-and-white, neutral color palette. Glass, metal, and concrete are widely used.", "ru": "Чистые линии, минималистский подход и в основном черно-белая, нейтральная цветовая палитра. Широко используются стекло, металл и бетон."},
    "ds_s2": {"uz": "Klassik (Classic)", "en": "Classic", "ru": "Классика"},
    "ds_s2_desc": {"uz": "Oltin va oqshom ranglari, o'ymakor naqshli yog'och mebellar, simmetrik tuzilish va hashamatli tuyg'u beruvchi og'ir matolar.", "en": "Gold and evening colors, carved wooden furniture, symmetrical structure, and heavy fabrics giving a luxurious feel.", "ru": "Золотые и вечерние цвета, резная деревянная мебель, симметричная структура и тяжелые ткани, придающие ощущение роскоши."},
    "ds_s3": {"uz": "Skandinav (Scandinavian)", "en": "Scandinavian", "ru": "Скандинавский"},
    "ds_s3_desc": {"uz": "Ochiq va yorqin xonalar, tabiiy yog'och fakturalari, iliqlik beruvchi pastel ohanglar. Asosiy maqsad – soddalik va qulaylik.", "en": "Bright and airy rooms, natural wood textures, warm pastel tones. Main goal – simplicity and comfort.", "ru": "Светлые и просторные комнаты, текстуры натурального дерева, теплые пастельные тона. Главная цель – простота и комфорт."},
    "ds_support": {"uz": "AI tomonidan qo'llab-quvvatlanadi", "en": "Supported by AI", "ru": "Поддерживается ИИ"},
    "ds_try": {"uz": "Sizga qaysi uslub ko'proq yoqadi?", "en": "Which style do you prefer?", "ru": "Какой стиль вам больше нравится?"},
    "ds_try_desc": {"uz": "Dasturda rasmingizni tahrirlayotganda ushbu dizayn uslublaridan birini tanlab maqsadli AI-generatsiyani sinab ko'ring.", "en": "Try targeted AI generation by selecting one of these design styles when editing your image in the program.", "ru": "Попробуйте целенаправленную ИИ-генерацию, выбрав один из этих стилей дизайна при редактировании изображения в программе."},
    "ds_btn": {"uz": "Dizayn yaratish", "en": "Create Design", "ru": "Создать дизайн"}
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
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

about_rep = {
    "Sun'iy intellekt yordamida interyer dizaynini yaratish": "{t('about_title')}",
    "Ushbu loyiha zamonaviy AI texnologiyalaridan foydalanib, rasmlardagi obyektlarni aniqlash va ularga mos ranglar palitrasini tavsiya etish imkonini beradi.": "{t('about_subtitle')}",
    "Loyiha maqsadi": "{t('about_goal')}",
    "Magistrlik dissertatsiyasi": "{t('about_thesis')}",
    "AI Color Designer dasturi interyer dizaynerlari, arxitektorlar va oddiy foydalanuvchilarga xona dizaynini yaratishda yordam berish uchun ishlab chiqilgan. Dastur insonning psixologik holatiga ijobiy ta'sir ko'rsatadigan ranglarni tanlash va ularni to'g'ridan-to'g'ri rasmdagi jihozlarga qo'llash imkoniyatini taqdim etadi.": "{t('about_desc')}",
    "Texnologiyalar": "{t('about_tech')}",
    "Stek va asboblar": "{t('about_stack')}",
    "Avtomatik obyektlarni aniqlash (Mask R-CNN)": "t('about_feat1')",
    "Ranglarning psixologik tahlili": "t('about_feat2')",
    "Mos keluvchi ranglar palitrasini tavsiya etish": "t('about_feat3')",
    "Tanlangan rangni rasmga real-vaqtda qo'llash": "t('about_feat4')",
    "Qo'shimcha": "{t('about_extra')}"
}
replace_in_file("About.tsx", about_rep)

ai_rep = {
    "Sun'iy intellekt tahlili": "{t('ai_title')}",
    "Mask R-CNN algoritmi yordamida rasmlardagi mebel va xona elementlarini avtomatik aniqlash jarayoni.": "{t('ai_desc')}",
    "Tasvirni skanerlash": "{t('ai_scan')}",
    "Yuklangan rasm piksellar kesimida tahlil qilinadi va chuqur neyron tarmoqlar yordamida xususiyatlar ajratib olinadi.": "{t('ai_scan_desc')}",
    "Obyektlarni ajratish": "{t('ai_seg')}",
    "Devor, poydevor, stol, divan kabi obyektlarning aniq chegaralari belgilanadi (Bounding Box va Segmentation Mask).": "{t('ai_seg_desc')}",
    "Qatlamli tahlil": "{t('ai_layer')}",
    "Har bir topilgan obyekt alohida qatlam sifatida saqlanib, keyinchalik faqat o'sha qismni bo'yash imkonini beradi.": "{t('ai_layer_desc')}",
    "O'z rasmingizni tahlil qilib ko'rasizmi?": "{t('ai_try')}",
    "Dasturimiz hozirda 80 dan ortiq uy jihozlari va arxitektura elementlarini taniy oladi. Hoziroq sinab ko'ring.": "{t('ai_try_desc')}",
    "Tahlilni boshlash": "{t('ai_start')}"
}
replace_in_file("AiAnalysis.tsx", ai_rep)

color_rep = {
    "Aqliy rang tavsiyalari": "{t('color_title')}",
    "Xonaning yorug'ligi, uslubi va maqsadiga qarab mukammal ranglar uyg'unligini yarating.": "{t('color_desc')}",
    "Ommabop palitralar": "{t('color_pop')}",
    '"Sokin Dengiz"': "t('color_p1')",
    '"Kuzgi Barglar"': "t('color_p2')",
    '"Minimalist Oq"': "t('color_p3')",
    '"Bahor Tongi"': "t('color_p4')",
    "Yorug'lik harorati": "{t('color_light')}",
    "Issiq yorug'lik xonaga shinamlik bersa, sovuq yorug'lik rasmiylik va kenglik tasavvurini uyg'otadi. Dastur buni hisobga olib rang taklif qiladi.": "{t('color_light_desc')}",
    "60-30-10 Qoidasi": "{t('color_rule')}",
    "60% asosiy rang (devorlar), 30% ikkilamchi rang (mebellar), 10% urg'u beruvchi rang (dekoratsiyalar). Bu oltin qoida dizaynni boyitadi.": "{t('color_rule_desc')}",
    "Xonangizga mos rang tanlaymizmi?": "{t('color_try')}",
    "Rasmingizni yuklang, AI unga mos ranglarni avtomatik tavsiya qiladi.": "{t('color_try_desc')}",
    "Rang tanlash": "{t('color_btn')}"
}
replace_in_file("ColorRec.tsx", color_rep)

mood_rep = {
    "Kayfiyat tahlili": "{t('mood_title')}",
    "Ranglar bizning his-tuyg'ularimiz va psixologiyamizga qanday ta'sir qilishini bilib oling.": "{t('mood_desc')}",
    '"Xotirjamlik"': "t('mood_m1')",
    '"Ko\'k va havorang ohanglar stressni kamaytiradi, diqqatni jamlashga yordam beradi. Yotoqxona uchun mos."': "t('mood_m1_desc')",
    '"G\'ayrat va Energiya"': "t('mood_m2')",
    '"Qizil va zarg\'aldoq ranglar ishtahani ochadi va harakatga undaydi. Oshxona va sport xonalariga xos."': "t('mood_m2_desc')",
    '"Issiqlik va Shinamlik"': "t('mood_m3')",
    '"Sariq, jigarrang kabi tuproq ranglari insonga qulaylik hissini beradi. Mehmonxonalar uchun ideal."': "t('mood_m3_desc')",
    '"Ijobiylik va Ijodkorlik"': "t('mood_m4')",
    '"Siyohrang va yashil ranglar tasavvurni kengaytirib, miya faoliyatini yaxshilaydi. Ish xonalariga mos."': "t('mood_m4_desc')",
    "Sizning uyingiz qanday kayfiyat beradi?": "{t('mood_try')}",
    "O'z rasmingizni tizimga yuklang va maqsadli kayfiyatni tanlab, AI yordamida dizayn yarating.": "{t('mood_try_desc')}",
    "Kayfiyat tahlili": "{t('mood_title')}"
}
replace_in_file("MoodAnalysis.tsx", mood_rep)

ds_rep = {
    "Dizayn uslubi": "{t('ds_title')}",
    "Arxitektura va interyer dizayn uslublari bilan tanishing hamda o'z uyingizni shu yo'nalishlarda bezating.": "{t('ds_desc')}",
    '"Modern (Zamonaviy)"': "t('ds_s1')",
    '"Toza chiziqlar, minimalist yondashuv va asosan oq-qora, neytral ranglar palitrasi. Shisha, metall va beton ko\'p ishlatiladi."': "t('ds_s1_desc')",
    '"Klassik (Classic)"': "t('ds_s2')",
    '"Oltin va oqshom ranglari, o\'ymakor naqshli yog\'och mebellar, simmetrik tuzilish va hashamatli tuyg\'u beruvchi og\'ir matolar."': "t('ds_s2_desc')",
    '"Skandinav (Scandinavian)"': "t('ds_s3')",
    '"Ochiq va yorqin xonalar, tabiiy yog\'och fakturalari, iliqlik beruvchi pastel ohanglar. Asosiy maqsad – soddalik va qulaylik."': "t('ds_s3_desc')",
    "AI tomonidan qo'llab-quvvatlanadi": "{t('ds_support')}",
    "Sizga qaysi uslub ko'proq yoqadi?": "{t('ds_try')}",
    "Dasturda rasmingizni tahrirlayotganda ushbu dizayn uslublaridan birini tanlab maqsadli AI-generatsiyani sinab ko'ring.": "{t('ds_try_desc')}",
    "Dizayn yaratish": "{t('ds_btn')}"
}
replace_in_file("DesignStyle.tsx", ds_rep)

# We must ensure `useTranslation` is imported for AiAnalysis, ColorRec, MoodAnalysis, DesignStyle
def ensure_translation_import(filename):
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "useTranslation" not in content:
        content = content.replace("import React from 'react';", "import React from 'react';\nimport { useTranslation } from 'react-i18next';")
        content = re.sub(r'export const (\w+) = \(\) => {', r'export const \1 = () => {\n  const { t } = useTranslation();', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

for f in ["AiAnalysis.tsx", "ColorRec.tsx", "MoodAnalysis.tsx", "DesignStyle.tsx"]:
    ensure_translation_import(f)

print("Static files localized successfully.")
