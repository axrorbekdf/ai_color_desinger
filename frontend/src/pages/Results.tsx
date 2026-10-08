import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { Layers, Image as ImageIcon, ArrowRight, Paintbrush, Loader2, Calendar, LayoutGrid, List } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../services/api';

export const Results = () => {
  const { t } = useTranslation();
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [viewMode, setViewMode] = useState<'grid' | 'list'>(() => {
    return (localStorage.getItem('resultsViewMode') as 'grid' | 'list') || 'grid';
  });
  const navigate = useNavigate();

  useEffect(() => {
    localStorage.setItem('resultsViewMode', viewMode);
  }, [viewMode]);

  useEffect(() => {
    fetchResults();
  }, []);

  const fetchResults = async () => {
    try {
      const res = await api.get('/projects/user/results');
      setResults(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const getImageUrl = (path: string) => {
    if (!path) return '';
    const baseUrl = import.meta.env.VITE_API_URL?.replace('/api/v1', '') || 'http://localhost:8000';
    return `${baseUrl}/storage/${path}`;
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <Loader2 className="w-8 h-8 text-indigo-500 animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-1">{t('results_title')}</h1>
          <p className="text-sm text-gray-500 dark:text-gray-400">{t('results_desc')}</p>
        </div>
        <div className="flex items-center gap-4">
          <div className="flex bg-gray-100 dark:bg-gray-800 p-1 rounded-xl">
            <button 
              onClick={() => setViewMode('grid')}
              className={`p-2 rounded-lg transition-colors ${viewMode === 'grid' ? 'bg-white dark:bg-[#2a2a2a] text-indigo-600 dark:text-indigo-400 shadow-sm' : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200'}`}
            >
              <LayoutGrid size={18} />
            </button>
            <button 
              onClick={() => setViewMode('list')}
              className={`p-2 rounded-lg transition-colors ${viewMode === 'list' ? 'bg-white dark:bg-[#2a2a2a] text-indigo-600 dark:text-indigo-400 shadow-sm' : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200'}`}
            >
              <List size={18} />
            </button>
          </div>
        </div>
      </div>

      {results.length === 0 ? (
        <div className="bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 p-12 text-center flex flex-col items-center">
          <div className="w-20 h-20 bg-gray-50 dark:bg-gray-800 rounded-full flex items-center justify-center mb-4">
            <Layers size={32} className="text-gray-400" />
          </div>
          <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-2">Hali natijalar yo'q</h2>
          <p className="text-gray-500 dark:text-gray-400 mb-6 max-w-sm">
            {t('results_empty_desc')}
          </p>
          <Link 
            to="/upload" 
            className="flex items-center gap-2 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 px-6 py-3 rounded-xl font-medium transition"
          >
            {t('start')} <ArrowRight size={18} />
          </Link>
        </div>
      ) : (
        <div className={viewMode === 'grid' ? "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" : "flex flex-col gap-4"}>
          {results.map((res) => {
            if (viewMode === 'grid') {
              return (
                <div 
                  key={res.id} 
                  className="group bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm hover:shadow-md border border-gray-100 dark:border-gray-800 overflow-hidden transition-all hover:-translate-y-1 flex flex-col"
                >
                  <div 
                    className="aspect-video bg-gray-100 dark:bg-gray-800 relative overflow-hidden cursor-pointer"
                    onClick={() => navigate(`/upload?projectId=${res.project_id}`)}
                  >
                    {res.result_image_path ? (
                      <img src={getImageUrl(res.result_image_path)} alt={res.name} className="w-full h-full object-cover" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center">
                        <ImageIcon size={32} className="text-gray-300 dark:text-gray-600" />
                      </div>
                    )}
                    <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                      <span className="bg-white text-gray-900 font-medium px-4 py-2 rounded-lg text-sm shadow-lg">{t('open_project')}</span>
                    </div>
                  </div>
                  
                  <div className="p-4 flex flex-col gap-2 flex-1">
                    <div className="flex justify-between items-start">
                      <div>
                        <h3 className="font-bold text-gray-900 dark:text-white truncate">{t('project_name')}: {res.project_name}</h3>
                        <p className="text-xs text-gray-500 font-medium mt-0.5 flex items-center gap-1">ID: #{res.id}</p>
                      </div>
                      <span className="text-[10px] bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 px-2 py-1 rounded-md font-bold">
                        {t('result')}
                      </span>
                    </div>
                    
                    <div className="bg-gray-50 dark:bg-gray-800/50 p-3 rounded-xl mt-1 flex-1">
                      <p className="text-sm text-gray-700 dark:text-gray-300 flex items-start gap-2">
                        <Paintbrush size={16} className="text-indigo-500 shrink-0 mt-0.5" />
                        <span>{res.action_description || 'Rang o\'zgartirildi'}</span>
                      </p>
                    </div>
                    
                    <div className="flex justify-between items-center mt-2 pt-3 border-t border-gray-100 dark:border-gray-800">
                      <span className="text-xs text-gray-500 flex items-center gap-1.5">
                        <Calendar size={12} />
                        {new Date(res.created_at).toLocaleDateString('uz-UZ', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}
                      </span>
                    </div>
                  </div>
                </div>
              );
            } else {
              return (
                <div 
                  key={res.id} 
                  onClick={() => navigate(`/upload?projectId=${res.project_id}`)}
                  className="group bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm hover:shadow-md border border-gray-100 dark:border-gray-800 overflow-hidden cursor-pointer transition-all flex items-stretch p-3 gap-4"
                >
                  <div className="w-40 h-28 rounded-lg bg-gray-100 dark:bg-gray-800 relative overflow-hidden shrink-0">
                    {res.result_image_path ? (
                      <img src={getImageUrl(res.result_image_path)} alt={res.name} className="w-full h-full object-cover" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center">
                        <ImageIcon size={24} className="text-gray-300 dark:text-gray-600" />
                      </div>
                    )}
                    <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                      <span className="bg-white text-gray-900 font-medium px-2.5 py-1.5 rounded-lg text-xs shadow-lg">{t('open')}</span>
                    </div>
                  </div>
                  
                  <div className="flex-1 min-w-0 flex flex-col justify-center py-1">
                    <div className="flex items-start justify-between">
                      <div>
                        <h3 className="font-bold text-lg text-gray-900 dark:text-white truncate">{res.project_name}</h3>
                        <p className="text-sm text-gray-500 font-medium mt-0.5">ID: #{res.id}</p>
                      </div>
                      <span className="text-xs text-gray-500 flex items-center gap-1.5 bg-gray-50 dark:bg-gray-800/50 px-2.5 py-1.5 rounded-lg">
                        <Calendar size={14} />
                        {new Date(res.created_at).toLocaleDateString('uz-UZ', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}
                      </span>
                    </div>
                    
                    <div className="mt-3 flex items-center gap-2">
                      <div className="w-8 h-8 rounded-full bg-indigo-50 dark:bg-indigo-900/30 flex items-center justify-center shrink-0">
                        <Paintbrush size={14} className="text-indigo-600 dark:text-indigo-400" />
                      </div>
                      <p className="text-sm font-medium text-gray-700 dark:text-gray-300 line-clamp-1">
                        {res.action_description || 'Rang o\'zgartirildi'}
                      </p>
                    </div>
                  </div>
                </div>
              );
            }
          })}
        </div>
      )}
    </div>
  );
};
