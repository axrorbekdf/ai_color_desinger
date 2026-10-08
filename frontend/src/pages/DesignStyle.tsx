import { Layers, CheckCircle2, ArrowRight } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

export const DesignStyle = () => {
  const { t } = useTranslation();
  const styles = [
    {
      title: t('ds_s1'),
      desc: t('ds_s1_desc'),
      img: "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80"
    },
    {
      title: t('ds_s2'),
      desc: t('ds_s2_desc'),
      img: "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=800&q=80"
    },
    {
      title: t('ds_s3'),
      desc: t('ds_s3_desc'),
      img: "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?auto=format&fit=crop&w=800&q=80"
    }
  ];

  return (
    <div className="max-w-5xl mx-auto flex flex-col gap-8 pb-10">
      <div className="bg-orange-500 rounded-3xl p-10 md:p-14 text-white shadow-sm relative overflow-hidden">
        <div className="absolute right-0 top-0 w-1/2 h-full opacity-10">
          <Layers size={300} className="absolute -right-10 -top-10" />
        </div>
        <div className="relative z-10 max-w-2xl">
          <h1 className="text-4xl font-extrabold mb-4">{t('ds_title')}</h1>
          <p className="text-lg text-orange-100">
            {t('ds_desc')}
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {styles.map((s, i) => (
          <div key={i} className="bg-white dark:bg-[#1a1a1a] rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 overflow-hidden flex flex-col hover:-translate-y-1 transition">
            <div className="h-48 relative overflow-hidden">
              <img src={s.img} alt={s.title} className="w-full h-full object-cover" />
            </div>
            <div className="p-6 flex-1 flex flex-col">
              <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-3">{s.title}</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-4 leading-relaxed flex-1">
                {s.desc}
              </p>
              <div className="flex items-center gap-1.5 text-xs font-semibold text-orange-500 bg-orange-50 dark:bg-orange-900/20 px-3 py-1.5 rounded-lg w-max">
                <CheckCircle2 size={14} /> {t('ds_support')}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-white dark:bg-[#1a1a1a] rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 p-8 flex flex-col md:flex-row items-center gap-8 justify-between mt-4">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-3">{t('ds_try')}</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            {t('ds_try_desc')}
          </p>
          <Link to="/upload" className="inline-flex items-center gap-2 bg-orange-500 hover:bg-orange-600 text-white px-6 py-3 rounded-xl font-medium transition">
            {t('ds_btn')} <ArrowRight size={18} />
          </Link>
        </div>
      </div>
    </div>
  );
};
