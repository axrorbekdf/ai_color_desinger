import { useState } from 'react';
import { Globe, Bell, Moon, Cpu, Save, CheckCircle2 } from 'lucide-react';
import { useTranslation } from 'react-i18next';

export const Settings = () => {
  const { t, i18n } = useTranslation();
  const [isSaved, setIsSaved] = useState(false);
  const [settings, setSettings] = useState({
    language: i18n.language || 'uz',
    notifications: true,
    aiModel: 'fast',
  });

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    i18n.changeLanguage(settings.language);
    localStorage.setItem('language', settings.language);
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 3000);
  };

  const toggleDarkMode = () => {
    document.documentElement.classList.toggle('dark');
  };

  return (
    <div className="max-w-4xl mx-auto flex flex-col gap-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-1">{t('settings.title')}</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">{t('settings.desc')}</p>
      </div>

      <div className="bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 p-6 md:p-8">
        <form onSubmit={handleSave} className="space-y-8 max-w-2xl">
          
          {/* Theme setting */}
          <div className="flex items-center justify-between pb-6 border-b border-gray-100 dark:border-gray-800">
            <div className="flex items-start gap-4">
               <div className="p-3 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 rounded-xl">
                 <Moon size={24} />
               </div>
               <div>
                 <h3 className="font-bold text-gray-900 dark:text-white mb-1">{t('settings.dark_mode')}</h3>
                 <p className="text-sm text-gray-500 dark:text-gray-400">{t('settings.dark_mode_desc')}</p>
               </div>
            </div>
            <button 
              type="button"
              onClick={toggleDarkMode}
              className="px-4 py-2 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm font-medium rounded-lg transition"
            >
              {t('settings.change_mode')}
            </button>
          </div>

          {/* Language setting */}
          <div className="flex items-center justify-between pb-6 border-b border-gray-100 dark:border-gray-800">
            <div className="flex items-start gap-4">
               <div className="p-3 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 rounded-xl">
                 <Globe size={24} />
               </div>
               <div>
                 <h3 className="font-bold text-gray-900 dark:text-white mb-1">{t('settings.language')}</h3>
                 <p className="text-sm text-gray-500 dark:text-gray-400">{t('settings.language_desc')}</p>
               </div>
            </div>
            <select 
              value={settings.language}
              onChange={e => setSettings({...settings, language: e.target.value})}
              className="bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-900 dark:text-white text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block p-2.5 outline-none"
            >
              <option value="uz">O'zbekcha</option>
              <option value="ru">Русский</option>
              <option value="en">English</option>
            </select>
          </div>

          {/* AI Model setting */}
          <div className="flex items-center justify-between pb-6 border-b border-gray-100 dark:border-gray-800">
            <div className="flex items-start gap-4">
               <div className="p-3 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 rounded-xl">
                 <Cpu size={24} />
               </div>
               <div>
                 <h3 className="font-bold text-gray-900 dark:text-white mb-1">{t('settings.ai_model')}</h3>
                 <p className="text-sm text-gray-500 dark:text-gray-400">{t('settings.ai_model_desc')}</p>
               </div>
            </div>
            <select 
              value={settings.aiModel}
              onChange={e => setSettings({...settings, aiModel: e.target.value})}
              className="bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-900 dark:text-white text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block p-2.5 outline-none"
            >
              <option value="fast">Tezkor (Mask R-CNN ResNet50)</option>
              <option value="accurate">Aniq (YOLOv8x-seg) - Tez kunda</option>
            </select>
          </div>

          {/* Notifications setting */}
          <div className="flex items-center justify-between pb-6 border-b border-gray-100 dark:border-gray-800">
            <div className="flex items-start gap-4">
               <div className="p-3 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 rounded-xl">
                 <Bell size={24} />
               </div>
               <div>
                 <h3 className="font-bold text-gray-900 dark:text-white mb-1">{t('settings.notifications')}</h3>
                 <p className="text-sm text-gray-500 dark:text-gray-400">{t('settings.notifications_desc')}</p>
               </div>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input 
                type="checkbox" 
                className="sr-only peer" 
                checked={settings.notifications}
                onChange={e => setSettings({...settings, notifications: e.target.checked})}
              />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-indigo-300 dark:peer-focus:ring-indigo-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-indigo-600"></div>
            </label>
          </div>

          <div className="pt-2 flex items-center gap-4">
            <button 
              type="submit" 
              className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-8 py-3 rounded-xl transition shadow-sm flex items-center gap-2"
            >
              <Save size={18} />
              {t('settings.save')}
            </button>
            {isSaved && (
              <span className="flex items-center gap-1.5 text-green-600 dark:text-green-400 text-sm font-medium animate-pulse">
                <CheckCircle2 size={16} /> {t('settings.saved')}
              </span>
            )}
          </div>
          
        </form>
      </div>
    </div>
  );
};
