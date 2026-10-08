import React from 'react';

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
  return (
    <div className="bg-white dark:bg-[#1a1a1a] rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-all hover:shadow-md">
      <div className="h-32 w-full" style={{ backgroundColor: rec.hex_val }}></div>
      
      <div className="p-5">
        <div className="flex justify-between items-start mb-2">
          <div>
            <h3 className="text-lg font-bold">{rec.color_name}</h3>
            <p className="text-sm text-gray-500 font-mono">{rec.hex_val}</p>
          </div>
          <div className="bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400 font-bold px-3 py-1 rounded-full text-sm">
            {rec.compatibility_score}% Match
          </div>
        </div>
        
        <p className="text-sm text-gray-600 dark:text-gray-400 mt-3 line-clamp-2" title={rec.recommendation_reason}>
          {rec.recommendation_reason}
        </p>
        
        <div className="grid grid-cols-2 gap-2 mt-4 text-xs">
          <div className="bg-gray-50 dark:bg-gray-800 p-2 rounded">
            <span className="block text-gray-500">Harmony</span>
            <span className="font-semibold">{rec.harmony_score}%</span>
          </div>
          <div className="bg-gray-50 dark:bg-gray-800 p-2 rounded">
            <span className="block text-gray-500">Mood</span>
            <span className="font-semibold">{rec.mood_score}%</span>
          </div>
        </div>
        
        <div className="mt-5 flex gap-2">
          <button 
            onClick={() => onApply(rec.id)}
            className="flex-1 bg-gray-900 dark:bg-white text-white dark:text-gray-900 py-2 rounded-lg font-medium hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors"
          >
            Apply Color
          </button>
        </div>
        
        {/* Simple Rating for thesis feedback */}
        <div className="mt-4 pt-4 border-t border-gray-100 dark:border-gray-800 flex justify-center space-x-1">
          {[1,2,3,4,5].map(star => (
            <button 
              key={star} 
              onClick={() => onRate(rec.id, star)}
              className="text-gray-300 hover:text-yellow-400 focus:text-yellow-400 text-xl"
            >
              ★
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};
