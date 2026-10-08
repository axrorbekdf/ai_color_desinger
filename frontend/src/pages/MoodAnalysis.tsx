import { Smile, Heart, Zap, Coffee, ArrowRight } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

export const MoodAnalysis = () => {
  const { t } = useTranslation();
  const moods = [
    { icon: Coffee, title: t('mood_m1'), color: "bg-blue-500", text: t('mood_m1_desc') },
    { icon: Zap, title: t('mood_m2'), color: "bg-red-500", text: t('mood_m2_desc') },
    { icon: Heart, title: t('mood_m3'), color: "bg-amber-500", text: t('mood_m3_desc') },
    { icon: Smile, title: t('mood_m4'), color: "bg-purple-500", text: t('mood_m4_desc') }
  ];

  return (
    <div className="max-w-5xl mx-auto flex flex-col gap-8 pb-10">
      <div className="bg-emerald-500 rounded-3xl p-10 md:p-14 text-white shadow-sm relative overflow-hidden">
        <div className="absolute right-0 top-0 w-1/2 h-full opacity-10">
          <Smile size={300} className="absolute -right-10 -top-10" />
        </div>
        <div className="relative z-10 max-w-2xl">
          <h1 className="text-4xl font-extrabold mb-4">{t('mood_title')}</h1>
          <p className="text-lg text-emerald-100">
            {t('mood_desc')}
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {moods.map((m, i) => (
          <div key={i} className="bg-white dark:bg-[#1a1a1a] p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 flex items-start gap-4 hover:-translate-y-1 transition">
            <div className={`w-14 h-14 rounded-2xl flex items-center justify-center text-white shrink-0 shadow-lg ${m.color}`}>
              <m.icon size={24} />
            </div>
            <div>
              <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{m.title}</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                {m.text}
              </p>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-white dark:bg-[#1a1a1a] rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 p-8 flex flex-col md:flex-row items-center gap-8 justify-between mt-4">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-3">{t('mood_try')}</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            {t('mood_try_desc')}
          </p>
          <Link to="/upload" className="inline-flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-white px-6 py-3 rounded-xl font-medium transition">
            {t('mood_title')} <ArrowRight size={18} />
          </Link>
        </div>
      </div>
    </div>
  );
};
