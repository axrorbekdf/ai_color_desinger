import React from 'react';
import { NavLink } from 'react-router-dom';
import { Upload, Cpu, Palette, Smile, Layers, ListTodo, Folder, Settings, Lightbulb } from 'lucide-react';
import clsx from 'clsx';

export const Sidebar = () => {
  const navItems = [
    { name: 'AI tahlili', path: '/ai-analysis', icon: Cpu },
    { name: 'Rang tavsiyasi', path: '/color-rec', icon: Palette },
    { name: 'Kayfiyat tahlili', path: '/mood-analysis', icon: Smile },
    { name: 'Dizayn uslubi', path: '/design-style', icon: Layers },
    { name: 'Natijalar', path: '/results', icon: ListTodo },
    { name: 'Loyihalarim', path: '/projects', icon: Folder },
    { name: 'Sozlamalar', path: '/settings', icon: Settings },
  ];

  return (
    <aside className="w-64 bg-[#f8f9fc] dark:bg-[#1a1a1a] h-full flex flex-col p-4 border-r border-gray-200 dark:border-gray-800">
      
      <button 
        onClick={() => {
          const btn = document.getElementById('upload-btn');
          if (btn) {
            btn.click();
          } else {
            window.location.href = '/upload';
          }
        }}
        className="w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl py-3 px-4 flex items-center justify-center gap-2 font-medium transition-colors mb-6 shadow-sm cursor-pointer"
      >
        <Upload size={20} />
        Rasm yuklash
      </button>

      <nav className="flex-1 space-y-1">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              clsx(
                "flex items-center space-x-3 px-4 py-3 rounded-xl transition-all duration-200 font-medium",
                isActive 
                  ? "text-indigo-600 bg-indigo-50 dark:bg-indigo-900/20 dark:text-indigo-400" 
                  : "text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800"
              )
            }
          >
            <item.icon size={20} />
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>

      <div className="mt-6 bg-indigo-50 dark:bg-indigo-900/10 p-4 rounded-2xl border border-indigo-100 dark:border-indigo-800/30">
        <div className="flex items-center gap-2 mb-2 text-indigo-700 dark:text-indigo-400 font-semibold">
          <Lightbulb size={20} className="text-yellow-500" />
          Maslahat
        </div>
        <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
          Rang nafaqat dizaynni, balki kayfiyatingizni ham o'zgartirishi mumkin.
        </p>
      </div>
    </aside>
  );
};
