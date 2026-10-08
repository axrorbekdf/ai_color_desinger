import re

for file in ['src/pages/Login.tsx', 'src/pages/Register.tsx']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # We replace any className that starts with w-full p-2 or w-full bg-gray-50
    # Let's just find the <input tag and replace its className
    c = re.sub(r'className="w-full[^"]+"', 'className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-2.5 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none transition"', c)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print('Input styles standardized')
