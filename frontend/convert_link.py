with open("src/pages/Dashboard.tsx", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace('<button className="text-sm text-indigo-600 dark:text-indigo-400 font-medium hover:underline flex items-center gap-1">\n            Barchasini ko\'rish <ArrowRight size={14} />\n            </button>',
              '<Link to="/projects" className="text-sm text-indigo-600 dark:text-indigo-400 font-medium hover:underline flex items-center gap-1">\n            {t(\'dashboard.see_all\')} <ArrowRight size={14} />\n            </Link>')

with open("src/pages/Dashboard.tsx", "w", encoding="utf-8") as f:
    f.write(c)
print("Button converted to Link")
