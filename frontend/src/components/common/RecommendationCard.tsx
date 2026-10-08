import React from 'react';
import { useTranslation } from 'react-i18next';
import { CheckCircle2, Info, Star } from 'lucide-react';

interface Recommendation {
  id: number;
  color_name: string;
  hex_val: string;
  compatibility_score: number;
  harmony_score: number;
  mood_score: number;
  recommendation_reason: string;
}

interface RecommendationCardProps {
  rec: Recommendation;
  onApply: (id: number) => void;
  onRate: (id: number, rating: number) => void;
}

export const RecommendationCard: React.FC<RecommendationCardProps> = ({ rec, onApply, onRate }) => {
  const { t } = useTranslation();
  return (
    <div className="bg-white dark:bg-[#1a1a1a] rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-all hover:shadow-md">
      <div className="h-32 w-full" style={{ backgroundColor: rec.hex_val }}></div>
      
      <div className="p-5">
        <div className="flex justify-between items-start mb-2">
          <div>
            <h3 className="text-lg font-bold">{rec.color_name}</h3>
            <p className="text-sm text-gray-500 font-mono">{rec.hex_val}</p>
          </div>
          <div className="bg-green-100 text-green-700 px-2 py-1 rounded text-xs font-bold">
            {rec.compatibility_score}% {t('components.rec_apply')}
          </div>
        </div>

        <p className="text-sm text-gray-600 dark:text-gray-400 mb-4 line-clamp-3">
          {rec.recommendation_reason}
        </p>

        <div className="grid grid-cols-2 gap-2 mb-4 text-xs">
          <div className="bg-gray-50 dark:bg-gray-800 p-2 rounded">
            <span className="text-gray-500 block mb-1">{t('components.rec_harmony')}</span>
            <div className="flex items-center">
              <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mr-2">
                <div className="bg-indigo-500 h-1.5 rounded-full" style={{ width: `${rec.harmony_score}%` }}></div>
              </div>
              <span className="font-bold">{rec.harmony_score}%</span>
            </div>
          </div>
          <div className="bg-gray-50 dark:bg-gray-800 p-2 rounded">
            <span className="text-gray-500 block mb-1">{t('components.rec_mood')}</span>
            <div className="flex items-center">
              <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mr-2">
                <div className="bg-pink-500 h-1.5 rounded-full" style={{ width: `${rec.mood_score}%` }}></div>
              </div>
              <span className="font-bold">{rec.mood_score}%</span>
            </div>
          </div>
        </div>

        <div className="flex gap-2">
          <button 
            onClick={() => onApply(rec.id)}
            className="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded-lg text-sm font-medium transition"
          >
            {t('components.rec_apply')}
          </button>
          <button className="p-2 border border-gray-200 dark:border-gray-700 text-gray-400 hover:text-yellow-400 hover:border-yellow-400 rounded-lg transition">
            <Star size={20} />
          </button>
        </div>
      </div>
    </div>
  );
};