import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { useNavigate, Link } from 'react-router-dom';
import { Eye, EyeOff } from 'lucide-react';
import api from '../services/api';
import { useAuthStore } from '../store/useAuthStore';

export const Login = () => {
  const { t } = useTranslation();
  const [email, setEmail] = useState('test@test.com');
  const [password, setPassword] = useState('123456');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const setToken = useAuthStore(state => state.setToken);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append('username', email); // OAuth2 expects username
      formData.append('password', password);
      
      const res = await api.post('/auth/login', formData);
      setToken(res.data.access_token);
      navigate('/');
    } catch (err) {
      setError("Login xatosi. Email yoki parol noto'g'ri.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-[#121212] relative">
      <div className="absolute top-4 right-4 flex gap-2">
        <button 
          onClick={() => document.documentElement.classList.toggle('dark')} 
          className="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 text-gray-500 dark:text-gray-400 transition bg-white dark:bg-[#1a1a1a] shadow-sm"
        >
          <span className="hidden dark:inline">🌙</span>
          <span className="inline dark:hidden">☀️</span>
        </button>
      </div>
      
      <div className="max-w-md w-full p-8 bg-white dark:bg-[#1a1a1a] rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold text-center mb-6 text-gray-900 dark:text-white">{t('auth.login_title')}</h2>
        {error && <div className="bg-red-100 text-red-600 p-3 rounded mb-4 text-sm">{error}</div>}
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">{t('auth.email')}</label>
            <input 
              type="email" 
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-2.5 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none transition" 
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">{t('auth.password')}</label>
            <div className="relative">
              <input 
                type={showPassword ? "text" : "password"}
                value={password}
                onChange={e => setPassword(e.target.value)}
                className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-2.5 pr-10 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none transition" 
                required
              />
              <button 
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition"
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
            </div>
          </div>
          <button type="submit" className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2.5 px-4 rounded-lg transition-colors">
            {t('auth.login_btn')}
          </button>
        </form>
        <p className="mt-4 text-center text-sm text-gray-600 dark:text-gray-400">
          {t('auth.no_account')} <Link to="/register" className="text-indigo-600 dark:text-indigo-400 font-medium hover:underline">{t('auth.register_link')}</Link>
        </p>
      </div>
    </div>
  );
};
