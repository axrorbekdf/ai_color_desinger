import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { Folder, Image as ImageIcon, Sparkles, Trash2, Edit3, Loader2, ArrowRight, LayoutGrid, List } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import { useToastStore } from '../store/useToastStore';
import api from '../services/api';

export const Projects = () => {
  const { t } = useTranslation();
  const [projects, setProjects] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [deleteConfirmId, setDeleteConfirmId] = useState<number | null>(null);
  const [viewMode, setViewMode] = useState<'grid' | 'list'>(() => {
    return (localStorage.getItem('projectsViewMode') as 'grid' | 'list') || 'grid';
  });
  const navigate = useNavigate();

  const { addToast } = useToastStore();

  useEffect(() => {
    localStorage.setItem('projectsViewMode', viewMode);
  }, [viewMode]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    try {
      const res = await api.get('/projects/');
      setProjects(res.data);
    } catch (err) {
      console.error(err);
      addToast('Loyihalarni yuklashda xatolik yuz berdi', 'error');
    } finally {
      setLoading(false);
    }
  };

  const confirmDelete = (e: React.MouseEvent, id: number) => {
    e.stopPropagation();
    setDeleteConfirmId(id);
  };

  const executeDelete = async () => {
    if (!deleteConfirmId) return;
    try {
      await api.delete(`/projects/${deleteConfirmId}`);
      setProjects(projects.filter(p => p.id !== deleteConfirmId));
      addToast('Loyiha muvaffaqiyatli o\'chirildi', 'success');
    } catch (err) {
      console.error(err);
      addToast('Loyihani o\'chirishda xatolik yuz berdi', 'error');
    } finally {
      setDeleteConfirmId(null);
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
    <div className="max-w-7xl mx-auto flex flex-col gap-6 relative">
      {/* Delete Confirmation Modal */}
      {deleteConfirmId && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
          <div className="bg-white dark:bg-[#1a1a1a] rounded-2xl p-6 max-w-sm w-full mx-4 shadow-xl border border-gray-100 dark:border-gray-800 animate-in fade-in zoom-in-95 duration-200">
            <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">O'chirishni tasdiqlaysizmi?</h3>
            <p className="text-gray-600 dark:text-gray-400 mb-6 text-sm">
              Bu loyiha va uning barcha amallar tarixi butunlay o'chib ketadi. Buni ortga qaytarib bo'lmaydi.
            </p>
            <div className="flex items-center justify-end gap-3">
              <button 
                onClick={() => setDeleteConfirmId(null)}
                className="px-4 py-2 rounded-xl text-gray-600 dark:text-gray-300 font-medium hover:bg-gray-100 dark:hover:bg-gray-800 transition"
              >
                Bekor qilish
              </button>
              <button 
                onClick={executeDelete}
                className="px-4 py-2 rounded-xl bg-red-500 hover:bg-red-600 text-white font-medium transition shadow-sm"
              >
                O'chirish
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-1">{t('projects_title')}</h1>
          <p className="text-sm text-gray-500 dark:text-gray-400">{t('projects_desc')}</p>
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
          <Link 
            to="/upload" 
            className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-xl font-medium transition shadow-sm"
          >
            <Sparkles size={18} />
            {t('new_image_upload')}
          </Link>
        </div>
      </div>

      {projects.length === 0 ? (
        <div className="bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 p-12 text-center flex flex-col items-center">
          <div className="w-20 h-20 bg-gray-50 dark:bg-gray-800 rounded-full flex items-center justify-center mb-4">
            <Folder size={32} className="text-gray-400" />
          </div>
          <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-2">{t('no_projects')}</h2>
          <p className="text-gray-500 dark:text-gray-400 mb-6 max-w-sm">
            {t('no_projects_desc')}
          </p>
          <Link 
            to="/upload" 
            className="flex items-center gap-2 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 px-6 py-3 rounded-xl font-medium transition"
          >
            {t('start_btn')} <ArrowRight size={18} />
          </Link>
        </div>
      ) : (
        <div className={viewMode === 'grid' ? "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6" : "flex flex-col gap-4"}>
          {projects.map((proj) => {
            const hasModified = !!proj.modified_image_path;
            const imgPath = hasModified ? proj.modified_image_path : proj.original_image_path;
            const objCount = proj.analysis_data?.objects?.length || 0;
            
            if (viewMode === 'grid') {
              return (
                <div 
                  key={proj.id} 
                  onClick={() => navigate(`/upload?projectId=${proj.id}`)}
                  className="group bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm hover:shadow-md border border-gray-100 dark:border-gray-800 overflow-hidden cursor-pointer transition-all hover:-translate-y-1"
                >
                  <div className="aspect-[4/3] bg-gray-100 dark:bg-gray-800 relative overflow-hidden">
                    {imgPath ? (
                      <img src={getImageUrl(imgPath)} alt={proj.name} className="w-full h-full object-cover" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center">
                        <ImageIcon size={32} className="text-gray-300 dark:text-gray-600" />
                      </div>
                    )}
                    <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-3">
                      <button className="bg-white/90 hover:bg-white text-gray-900 w-10 h-10 rounded-full flex items-center justify-center shadow-lg transition">
                        <Edit3 size={18} />
                      </button>
                      <button 
                        onClick={(e) => confirmDelete(e, proj.id)}
                        className="bg-red-500/90 hover:bg-red-500 text-white w-10 h-10 rounded-full flex items-center justify-center shadow-lg transition"
                      >
                        <Trash2 size={18} />
                      </button>
                    </div>
                    {hasModified && (
                      <div className="absolute top-3 left-3 bg-indigo-500 text-white text-[10px] font-bold px-2 py-1 rounded-md shadow-sm">
                        Tahrirlangan
                      </div>
                    )}
                  </div>
                  <div className="p-4 border-t border-gray-100 dark:border-gray-800">
                    <h3 className="font-bold text-gray-900 dark:text-white truncate">{proj.name || t('new_project')}</h3>
                    <div className="flex items-center justify-between mt-2">
                      <p className="text-xs text-gray-500 dark:text-gray-400">
                        {new Date(proj.created_at).toLocaleDateString('uz-UZ', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}
                      </p>
                      <span className="text-[10px] font-semibold bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 px-2 py-1 rounded-full">
                        {objCount} obyekt
                      </span>
                    </div>
                  </div>
                </div>
              );
            } else {
              return (
                <div 
                  key={proj.id} 
                  onClick={() => navigate(`/upload?projectId=${proj.id}`)}
                  className="group bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm hover:shadow-md border border-gray-100 dark:border-gray-800 overflow-hidden cursor-pointer transition-all flex items-center p-3 gap-4"
                >
                  <div className="w-32 h-24 rounded-lg bg-gray-100 dark:bg-gray-800 relative overflow-hidden shrink-0">
                    {imgPath ? (
                      <img src={getImageUrl(imgPath)} alt={proj.name} className="w-full h-full object-cover" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center">
                        <ImageIcon size={24} className="text-gray-300 dark:text-gray-600" />
                      </div>
                    )}
                    {hasModified && (
                      <div className="absolute top-2 left-2 bg-indigo-500 text-white text-[9px] font-bold px-1.5 py-0.5 rounded shadow-sm">
                        Tahrirlangan
                      </div>
                    )}
                  </div>
                  <div className="flex-1 min-w-0 flex flex-col justify-center">
                    <h3 className="font-bold text-lg text-gray-900 dark:text-white truncate">{proj.name || t('new_project')}</h3>
                    <div className="flex items-center gap-4 mt-1">
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {new Date(proj.created_at).toLocaleDateString('uz-UZ', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}
                      </p>
                      <span className="text-xs font-semibold bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 px-2.5 py-1 rounded-full">
                        {objCount} {t('objects_found')}
                      </span>
                    </div>
                  </div>
                  <div className="flex items-center gap-2 px-4 opacity-0 group-hover:opacity-100 transition-opacity">
                    <button className="bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-900 dark:text-white w-10 h-10 rounded-full flex items-center justify-center transition">
                      <Edit3 size={18} />
                    </button>
                    <button 
                      onClick={(e) => confirmDelete(e, proj.id)}
                      className="bg-red-50 dark:bg-red-900/20 hover:bg-red-100 dark:hover:bg-red-900/40 text-red-600 dark:text-red-400 w-10 h-10 rounded-full flex items-center justify-center transition"
                    >
                      <Trash2 size={18} />
                    </button>
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
