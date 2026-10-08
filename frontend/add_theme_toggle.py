for file in ['src/pages/Login.tsx', 'src/pages/Register.tsx']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    button_html = '''
    <div className="absolute top-4 right-4 flex gap-2">
        <button 
          onClick={() => document.documentElement.classList.toggle('dark')} 
          className="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 text-gray-500 dark:text-gray-400 transition bg-white dark:bg-[#1a1a1a] shadow-sm"
        >
          <span className="hidden dark:inline">🌙</span>
          <span className="inline dark:hidden">☀️</span>
        </button>
    </div>
    '''
    
    c = c.replace('<div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-[#121212]">', '<div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-[#121212] relative">' + button_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print('Added theme toggle to Login and Register')
