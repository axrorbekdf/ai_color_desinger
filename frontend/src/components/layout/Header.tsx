import { useTranslation } from 'react-i18next';
import { NavLink } from 'react-router-dom';
import { Home, Upload, Palette, Smile, Folder, Info } from 'lucide-react';
import clsx from 'clsx';

export const Header = () => {
  const { t } = useTranslation();

  const navItems = [
    { name: t("sidebar.dashboard"), path: '/', icon: Home },
    { name: t("sidebar.upload"), path: '/upload', icon: Upload },
    { name: t("sidebar.color_rec"), path: '/color-rec', icon: Palette },
    { name: t("sidebar.mood_analysis"), path: '/mood-analysis', icon: Smile },
    { name: t("sidebar.projects"), path: '/projects', icon: Folder },
    { name: t("sidebar.about"), path: '/about', icon: Info },
  ];

  return (
    <header className="bg-[#f8f9fc] dark:bg-[#121212] py-4 px-8 flex justify-between items-center border-b border-gray-200 dark:border-gray-800">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-pink-500 via-red-500 to-yellow-500 flex items-center justify-center p-1">
           {/* Fake logo icon */}
           <div className="w-full h-full rounded-full bg-white opacity-20"></div>
        </div>
        <div>
          <h1 className="text-xl font-bold text-gray-900 dark:text-white">AI Color Designer</h1>
          <p className="text-xs text-gray-500">Rang orqali go'zal dizayn va yaxshi kayfiyat</p>
        </div>
      </div>
      
      <nav className="flex items-center space-x-2">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              clsx(
                "flex items-center space-x-2 px-4 py-2 rounded-xl transition-all duration-200 font-medium text-sm",
                isActive 
                  ? "bg-indigo-100 text-indigo-700 dark:bg-indigo-900/30 dark:text-indigo-300" 
                  : "text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800"
              )
            }
          >
            <item.icon size={16} />
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>
      
      <div className="flex items-center space-x-4">
        <button 
          onClick={() => document.documentElement.classList.toggle('dark')} 
          className="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 text-gray-500 dark:text-gray-400 transition"
          title="Tungi/Kunduzgi rejim"
        >
          <span className="hidden dark:inline">☀️</span>
          <span className="inline dark:hidden">🌙</span>
        </button>
        <NavLink to="/profile" className="flex items-center space-x-3 border-l border-gray-300 dark:border-gray-700 pl-4 hover:opacity-80 transition cursor-pointer">
          <img src="https://i.pravatar.cc/150?u=a042581f4e29026704d" alt="User" className="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-700" />
          <span className="font-medium text-sm text-gray-800 dark:text-gray-200">{t('header.user')}</span>
        </NavLink>
      </div>
    </header>
  );
};
