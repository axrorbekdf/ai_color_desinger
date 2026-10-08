import { NavLink } from 'react-router-dom';
import { Upload, Cpu, Palette, Smile, Layers, ListTodo, Folder, Settings, Lightbulb } from 'lucide-react';
import clsx from 'clsx';
import { useTranslation } from 'react-i18next';

export const Sidebar = () => {
  const { t } = useTranslation();

  const navItems = [
    { name: t('sidebar.ai_analysis'), path: '/ai-analysis', icon: Cpu },
    { name: t('sidebar.color_rec'), path: '/color-rec', icon: Palette },
    { name: t('sidebar.mood_analysis'), path: '/mood-analysis', icon: Smile },
    { name: t('sidebar.design_style'), path: '/design-style', icon: Layers },
    { name: t('sidebar.results'), path: '/results', icon: ListTodo },
    { name: t('sidebar.projects'), path: '/projects', icon: Folder },
    { name: t('sidebar.settings'), path: '/settings', icon: Settings },
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
        {t('sidebar.upload')}
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
          {t('sidebar.tip_title')}
        </div>
        <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
          {t('sidebar.tip_desc')}
        </p>
      </div>
    </aside>
  );
};
