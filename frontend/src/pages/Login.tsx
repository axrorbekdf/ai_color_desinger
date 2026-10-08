import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import { useAuthStore } from '../store/useAuthStore';

export const Login = () => {
  const [email, setEmail] = useState('test@test.com');
  const [password, setPassword] = useState('123456');
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
    <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-[#121212]">
      <div className="max-w-md w-full p-8 bg-white dark:bg-[#1a1a1a] rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold text-center mb-6 text-gray-900 dark:text-white">Tizimga kirish</h2>
        {error && <div className="bg-red-100 text-red-600 p-3 rounded mb-4 text-sm">{error}</div>}
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Email</label>
            <input 
              type="email" 
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700" 
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Parol</label>
            <input 
              type="password" 
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700" 
              required
            />
          </div>
          <button type="submit" className="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded">
            Kirish
          </button>
        </form>
        <p className="mt-4 text-center text-sm text-gray-600 dark:text-gray-400">
          Akkauntingiz yo'qmi? <Link to="/register" className="text-green-500 font-medium">Ro'yxatdan o'tish</Link>
        </p>
      </div>
    </div>
  );
};
