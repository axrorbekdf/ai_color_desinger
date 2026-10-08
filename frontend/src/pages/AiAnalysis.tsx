import { Cpu, Scan, Box, Layers, ArrowRight } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

export const AiAnalysis = () => {
  const { t } = useTranslation();
  return (
    <div className="max-w-5xl mx-auto flex flex-col gap-8 pb-10">
      <div className="bg-indigo-600 rounded-3xl p-10 md:p-14 text-white shadow-sm relative overflow-hidden">
        <div className="absolute right-0 top-0 w-1/2 h-full opacity-10">
          <Cpu size={300} className="absolute -right-10 -top-10" />
        </div>
        <div className="relative z-10 max-w-2xl">
          <h1 className="text-4xl font-extrabold mb-4">{t('ai_title')}</h1>
          <p className="text-lg text-indigo-100">
            {t('ai_desc')}
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800">
          <div className="w-12 h-12 bg-blue-50 dark:bg-blue-900/30 rounded-2xl flex items-center justify-center text-blue-600 dark:text-blue-400 mb-4">
            <Scan size={24} />
          </div>
          <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{t('ai_scan')}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            {t('ai_scan_desc')}
          </p>
        </div>

        <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800">
          <div className="w-12 h-12 bg-purple-50 dark:bg-purple-900/30 rounded-2xl flex items-center justify-center text-purple-600 dark:text-purple-400 mb-4">
            <Box size={24} />
          </div>
          <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{t('ai_seg')}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            {t('ai_seg_desc')}
          </p>
        </div>

        <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800">
          <div className="w-12 h-12 bg-green-50 dark:bg-green-900/30 rounded-2xl flex items-center justify-center text-green-600 dark:text-green-400 mb-4">
            <Layers size={24} />
          </div>
          <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{t('ai_layer')}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            {t('ai_layer_desc')}
          </p>
        </div>
      </div>

      <div className="bg-white dark:bg-[#1a1a1a] rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 p-8 flex flex-col md:flex-row items-center gap-8 justify-between">
        <div className="max-w-xl">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-3">{t('ai_try')}</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            {t('ai_try_desc')}
          </p>
          <Link to="/upload" className="inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-xl font-medium transition">
            {t('ai_start')} <ArrowRight size={18} />
          </Link>
        </div>
        <div className="w-full md:w-1/3 bg-gray-50 dark:bg-gray-800 rounded-2xl h-48 flex items-center justify-center relative overflow-hidden border border-gray-100 dark:border-gray-700">
          <div className="absolute inset-x-0 h-[2px] bg-indigo-500/50 top-1/2 animate-scan"></div>
          <Cpu size={48} className="text-indigo-500" />
        </div>
      </div>
    </div>
  );
};
