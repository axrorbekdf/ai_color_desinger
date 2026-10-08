import { Palette, Droplet, Sun, ArrowRight } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

export const ColorRec = () => {
  const { t } = useTranslation();
  const palettes = [
    { name: t('color_p1'), colors: ["#0f172a", "#1e293b", "#334155", "#475569", "#94a3b8"] },
    { name: t('color_p2'), colors: ["#7c2d12", "#9a3412", "#c2410c", "#ea580c", "#f97316"] },
    { name: t('color_p3'), colors: ["#fafafa", "#f5f5f5", "#e5e5e5", "#d4d4d4", "#a3a3a3"] },
    { name: t('color_p4'), colors: ["#14532d", "#166534", "#15803d", "#16a34a", "#22c55e"] }
  ];

  return (
    <div className="max-w-5xl mx-auto flex flex-col gap-8 pb-10">
      <div className="bg-rose-500 rounded-3xl p-10 md:p-14 text-white shadow-sm relative overflow-hidden">
        <div className="absolute right-0 top-0 w-1/2 h-full opacity-10">
          <Palette size={300} className="absolute -right-10 -top-10" />
        </div>
        <div className="relative z-10 max-w-2xl">
          <h1 className="text-4xl font-extrabold mb-4">{t('color_title')}</h1>
          <p className="text-lg text-rose-100">
            {t('color_desc')}
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-[#1a1a1a] p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6 flex items-center gap-2">
            <Palette className="text-rose-500" /> {t('color_pop')}
          </h2>
          <div className="space-y-6">
            {palettes.map((p, i) => (
              <div key={i}>
                <p className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">{p.name}</p>
                <div className="flex rounded-lg overflow-hidden h-12 shadow-sm">
                  {p.colors.map((c, j) => (
                    <div key={j} className="flex-1 transition-all hover:flex-[1.5]" style={{ backgroundColor: c }}></div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="flex flex-col gap-6">
          <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 flex-1">
            <div className="w-12 h-12 bg-amber-50 dark:bg-amber-900/30 rounded-2xl flex items-center justify-center text-amber-500 mb-4">
              <Sun size={24} />
            </div>
            <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{t('color_light')}</h3>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {t('color_light_desc')}
            </p>
          </div>
          
          <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 flex-1">
            <div className="w-12 h-12 bg-cyan-50 dark:bg-cyan-900/30 rounded-2xl flex items-center justify-center text-cyan-500 mb-4">
              <Droplet size={24} />
            </div>
            <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{t('color_rule')}</h3>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {t('color_rule_desc')}
            </p>
          </div>
        </div>
      </div>

      <div className="bg-white dark:bg-[#1a1a1a] rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 p-8 flex flex-col md:flex-row items-center gap-8 justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-3">{t('color_try')}</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            {t('color_try_desc')}
          </p>
          <Link to="/upload" className="inline-flex items-center gap-2 bg-rose-500 hover:bg-rose-600 text-white px-6 py-3 rounded-xl font-medium transition">
            {t('color_btn')} <ArrowRight size={18} />
          </Link>
        </div>
      </div>
    </div>
  );
};
