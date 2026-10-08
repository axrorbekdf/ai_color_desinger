for file in ['src/pages/Login.tsx', 'src/pages/Register.tsx']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # restore button classes
    c = c.replace('<button type="submit" className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-2.5 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none transition">\n            {t(\'auth.login_btn\')}', '<button type="submit" className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2.5 px-4 rounded-lg transition-colors">\n            {t(\'auth.login_btn\')}')
    
    c = c.replace('<button type="submit" className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-2.5 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none transition">\n            {t(\'auth.register_link\')}', '<button type="submit" className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2.5 px-4 rounded-lg transition-colors">\n            {t(\'auth.register_link\')}')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print('Buttons restored')
