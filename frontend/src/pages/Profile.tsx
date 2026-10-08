import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { User as UserIcon, Mail, Lock, Shield, LogOut, CheckCircle2, Eye, EyeOff } from 'lucide-react';
import { useAuthStore } from '../store/useAuthStore';
import { useNavigate } from 'react-router-dom';

export const Profile = () => {
  const { t } = useTranslation();
  const { logout } = useAuthStore();
  const navigate = useNavigate();
  
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [showCurrentPassword, setShowCurrentPassword] = useState(false);
  const [showNewPassword, setShowNewPassword] = useState(false);
  const [isSaved, setIsSaved] = useState(false);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    // Simulate save
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 3000);
    setCurrentPassword('');
    setNewPassword('');
  };

  return (
    <div className="max-w-4xl mx-auto flex flex-col gap-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-1">{t('profile.profile_title')}</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">{t('profile.profile_desc')}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Profile Card */}
        <div className="col-span-1 bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 p-6 flex flex-col items-center text-center">
          <div className="w-24 h-24 rounded-full border-4 border-indigo-50 dark:border-indigo-900/30 overflow-hidden mb-4">
            <img src="https://i.pravatar.cc/150?u=a042581f4e29026704d" alt="Profile" className="w-full h-full object-cover" />
          </div>
          <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-1">{t('header.user')}</h2>
          <p className="text-sm text-gray-500 dark:text-gray-400 flex items-center justify-center gap-1.5 mb-6">
             <Shield size={14} className="text-green-500" />
             {t('profile.active_user')}
          </p>
          
          <div className="w-full bg-gray-50 dark:bg-gray-800 rounded-xl p-4 mb-6">
            <div className="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300 mb-2 border-b border-gray-200 dark:border-gray-700 pb-2">
               <UserIcon size={16} /> <span>admin</span>
            </div>
            <div className="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
               <Mail size={16} /> <span>admin@aicolor.uz</span>
            </div>
          </div>

          <button 
            onClick={handleLogout}
            className="w-full mt-auto flex items-center justify-center gap-2 py-2.5 rounded-xl border border-red-200 dark:border-red-900/50 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 transition font-medium"
          >
            <LogOut size={18} />
            {t('profile.logout')}
          </button>
        </div>

        {/* Edit Profile Form */}
        <div className="col-span-1 md:col-span-2 bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 p-6">
          <h3 className="font-bold text-lg text-gray-900 dark:text-white mb-6 border-b border-gray-100 dark:border-gray-800 pb-4 flex items-center gap-2">
            <Lock size={20} className="text-indigo-500" />
            {t('profile.change_password')}
          </h3>
          
          <form onSubmit={handleSave} className="space-y-5 max-w-md">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">{t('profile.current_password')}</label>
              <div className="relative">
                  <input 
                    type={showCurrentPassword ? "text" : "password"}
                    value={currentPassword}
                    onChange={e => setCurrentPassword(e.target.value)}
                    className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-2.5 pr-10 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition" 
                    placeholder="••••••••"
                  />
                  <button 
                    type="button"
                    onClick={() => setShowCurrentPassword(!showCurrentPassword)}
                    className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition"
                  >
                    {showCurrentPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                  </button>
                </div>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">{t('profile.new_password')}</label>
              <div className="relative">
                  <input 
                    type={showNewPassword ? "text" : "password"}
                    value={newPassword}
                    onChange={e => setNewPassword(e.target.value)}
                    className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-2.5 pr-10 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition" 
                    placeholder="••••••••"
                  />
                  <button 
                    type="button"
                    onClick={() => setShowNewPassword(!showNewPassword)}
                    className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition"
                  >
                    {showNewPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                  </button>
                </div>
            </div>
            <div className="pt-2 flex items-center gap-4">
              <button 
                type="submit" 
                className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-6 py-2.5 rounded-xl transition shadow-sm"
              >
                Saqlash
              </button>
              {isSaved && (
                <span className="flex items-center gap-1.5 text-green-600 dark:text-green-400 text-sm font-medium animate-pulse">
                  <CheckCircle2 size={16} /> {t('profile.saved_success')}
                </span>
              )}
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};
