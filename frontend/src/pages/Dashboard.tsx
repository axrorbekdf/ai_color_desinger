import React from 'react';
import { useTranslation } from 'react-i18next';

export const Dashboard = () => {
  const { t } = useTranslation();

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">{t('sidebar.dashboard')}</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800">
          <h3 className="text-lg font-medium text-gray-500">Total Projects</h3>
          <p className="text-4xl font-bold mt-2">0</p>
        </div>
        <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800">
          <h3 className="text-lg font-medium text-gray-500">Analyzed Images</h3>
          <p className="text-4xl font-bold mt-2">0</p>
        </div>
        <div className="bg-white dark:bg-[#1a1a1a] p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800">
          <h3 className="text-lg font-medium text-gray-500">Color Recommendations</h3>
          <p className="text-4xl font-bold mt-2">0</p>
        </div>
      </div>

      <div className="bg-white dark:bg-[#1a1a1a] p-8 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 text-center mt-8">
        <p className="text-gray-500">Hali loyihalar yo'q. Birinchi rasmni yuklang va AI tahlilini boshlang!</p>
      </div>
    </div>
  );
};
