import { Sparkles, Brain, Code2, Database, Rocket, GraduationCap, LayoutGrid } from 'lucide-react';
import { useTranslation } from 'react-i18next';

export const About = () => {
  const { t } = useTranslation();

  return (
    <div className="max-w-5xl mx-auto flex flex-col gap-8 pb-10">
      
      {/* Hero Section */}
      <div className="bg-gradient-to-br from-indigo-600 to-purple-700 rounded-3xl p-10 md:p-14 text-white relative overflow-hidden shadow-lg">
        <div className="absolute top-0 right-0 w-96 h-96 bg-white/10 blur-[100px] rounded-full translate-x-1/3 -translate-y-1/3"></div>
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-black/10 blur-[100px] rounded-full -translate-x-1/3 translate-y-1/3"></div>
        
        <div className="relative z-10 max-w-2xl">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/20 border border-white/30 backdrop-blur-sm text-sm font-medium mb-6">
            <Sparkles size={16} /> AI Color Designer
          </div>
          <h1 className="text-4xl md:text-5xl font-extrabold leading-tight mb-6">
            {t('about_title')}
          </h1>
          <p className="text-lg md:text-xl text-indigo-100 leading-relaxed">
            {t('about_subtitle')}
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Project Info */}
        <div className="bg-white dark:bg-[#1a1a1a] p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-12 h-12 bg-indigo-50 dark:bg-indigo-900/30 rounded-2xl flex items-center justify-center text-indigo-600 dark:text-indigo-400">
              <GraduationCap size={24} />
            </div>
            <div>
              <h2 className="text-xl font-bold text-gray-900 dark:text-white">{t('about_goal')}</h2>
              <p className="text-sm text-gray-500 dark:text-gray-400">{t('about_thesis')}</p>
            </div>
          </div>
          <p className="text-gray-600 dark:text-gray-300 leading-relaxed mb-6 text-sm">
            {t('about_desc')}
          </p>
          <ul className="space-y-3">
            {[
              "t('about_feat1')",
              "t('about_feat2')",
              "t('about_feat3')",
              "t('about_feat4')"
            ].map((item, i) => (
              <li key={i} className="flex items-center gap-3 text-sm font-medium text-gray-700 dark:text-gray-300">
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-500"></div>
                {item}
              </li>
            ))}
          </ul>
        </div>

        {/* Technologies */}
        <div className="bg-white dark:bg-[#1a1a1a] p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-12 h-12 bg-purple-50 dark:bg-purple-900/30 rounded-2xl flex items-center justify-center text-purple-600 dark:text-purple-400">
              <Code2 size={24} />
            </div>
            <div>
              <h2 className="text-xl font-bold text-gray-900 dark:text-white">{t('about_tech')}</h2>
              <p className="text-sm text-gray-500 dark:text-gray-400">{t('about_stack')}</p>
            </div>
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-gray-50 dark:bg-gray-800/50 p-4 rounded-2xl border border-gray-100 dark:border-gray-800 transition hover:-translate-y-1">
              <Brain className="text-blue-500 mb-2" size={20} />
              <h3 className="font-bold text-sm text-gray-900 dark:text-white mb-1">AI & ML</h3>
              <p className="text-xs text-gray-500">PyTorch, Mask R-CNN, OpenCV</p>
            </div>
            
            <div className="bg-gray-50 dark:bg-gray-800/50 p-4 rounded-2xl border border-gray-100 dark:border-gray-800 transition hover:-translate-y-1">
              <Database className="text-emerald-500 mb-2" size={20} />
              <h3 className="font-bold text-sm text-gray-900 dark:text-white mb-1">Backend</h3>
              <p className="text-xs text-gray-500">FastAPI, Python, SQLAlchemy, MySQL</p>
            </div>
            
            <div className="bg-gray-50 dark:bg-gray-800/50 p-4 rounded-2xl border border-gray-100 dark:border-gray-800 transition hover:-translate-y-1">
              <LayoutGrid className="text-orange-500 mb-2" size={20} />
              <h3 className="font-bold text-sm text-gray-900 dark:text-white mb-1">Frontend</h3>
              <p className="text-xs text-gray-500">React, TypeScript, TailwindCSS v4, Vite</p>
            </div>
            
            <div className="bg-gray-50 dark:bg-gray-800/50 p-4 rounded-2xl border border-gray-100 dark:border-gray-800 transition hover:-translate-y-1">
              <Rocket className="text-indigo-500 mb-2" size={20} />
              <h3 className="font-bold text-sm text-gray-900 dark:text-white mb-1">{t('about_extra')}</h3>
              <p className="text-xs text-gray-500">Recharts, Lucide, JWT Auth, i18next</p>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  );
};
