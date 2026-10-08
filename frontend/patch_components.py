import json
import os

locales_dir = "d:/Projects/ai_color_desinger/frontend/src/locales"

additions = {
    "slider_original": {"uz": "Original", "en": "Original", "ru": "Оригинал"},
    "slider_recolored": {"uz": "Tahrirlangan", "en": "Recolored", "ru": "Отредактировано"},
    "rec_apply": {"uz": "Qo'llash", "en": "Apply Color", "ru": "Применить цвет"},
    "rec_harmony": {"uz": "Uyg'unlik", "en": "Harmony", "ru": "Гармония"},
    "rec_mood": {"uz": "Kayfiyat", "en": "Mood", "ru": "Настроение"}
}

for lang in ["uz", "en", "ru"]:
    path = os.path.join(locales_dir, lang, "translation.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "components" not in data:
        data["components"] = {}
        
    for k, v in additions.items():
        data["components"][k] = v[lang]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

with open("d:/Projects/ai_color_desinger/frontend/src/components/common/BeforeAfterSlider.tsx", "r", encoding="utf-8") as f:
    c = f.read()

if "import { useTranslation } from 'react-i18next';" not in c:
    c = c.replace("import React,", "import React, { useState, useRef, useEffect } from 'react';\nimport { useTranslation } from 'react-i18next';\n")
if "const { t } = useTranslation();" not in c:
    c = c.replace("export const BeforeAfterSlider: React.FC<BeforeAfterSliderProps> = ({ beforeImage, afterImage }) => {", "export const BeforeAfterSlider: React.FC<BeforeAfterSliderProps> = ({ beforeImage, afterImage }) => {\n  const { t } = useTranslation();")
    
c = c.replace(">Original<", ">{t('components.slider_original')}<")
c = c.replace(">Recolored<", ">{t('components.slider_recolored')}<")

with open("d:/Projects/ai_color_desinger/frontend/src/components/common/BeforeAfterSlider.tsx", "w", encoding="utf-8") as f:
    f.write(c)


with open("d:/Projects/ai_color_desinger/frontend/src/components/common/RecommendationCard.tsx", "r", encoding="utf-8") as f:
    c = f.read()

if "import { useTranslation } from 'react-i18next';" not in c:
    c = c.replace("import React", "import React from 'react';\nimport { useTranslation } from 'react-i18next';\n")
if "const { t } = useTranslation();" not in c:
    c = c.replace("export const RecommendationCard: React.FC<RecommendationCardProps> = ({", "export const RecommendationCard: React.FC<RecommendationCardProps> = ({\n")
    c = c.replace("  onApply", "  onApply\n}) => {\n  const { t } = useTranslation();")
    c = c.replace("}) => {", "") # clean up original line
    c = c.replace("export const RecommendationCard: React.FC<RecommendationCardProps> = ({\n\n  onApply\n}) => {\n  const { t } = useTranslation();", "export const RecommendationCard: React.FC<RecommendationCardProps> = ({ recommendation, isSelected, onSelect, onApply }) => {\n  const { t } = useTranslation();") # safe hardcode

c = c.replace(">Apply Color<", ">{t('components.rec_apply')}<")
c = c.replace(">Harmony<", ">{t('components.rec_harmony')}<")
c = c.replace(">Mood<", ">{t('components.rec_mood')}<")

with open("d:/Projects/ai_color_desinger/frontend/src/components/common/RecommendationCard.tsx", "w", encoding="utf-8") as f:
    f.write(c)

print("Components patched")
