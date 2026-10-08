import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';

export const Register = () => {
  const [name, setName] = useState('Tester');
  const [email, setEmail] = useState('test@test.com');
  const [password, setPassword] = useState('123456');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/auth/register', { name, email, password });
      navigate('/login');
    } catch (err) {
      setError("Ro'yxatdan o'tishda xatolik yuz berdi.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-[#121212]">
      <div className="max-w-md w-full p-8 bg-white dark:bg-[#1a1a1a] rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold text-center mb-6 text-gray-900 dark:text-white">Ro'yxatdan o'tish</h2>
        {error && <div className="bg-red-100 text-red-600 p-3 rounded mb-4 text-sm">{error}</div>}
        <form onSubmit={handleRegister} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Ism</label>
            <input 
              type="text" 
              value={name}
              onChange={e => setName(e.target.value)}
              className="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700" 
              required
            />
          </div>
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
              minLength={6}
            />
          </div>
          <button type="submit" className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
            Ro'yxatdan o'tish
          </button>
        </form>
        <p className="mt-4 text-center text-sm text-gray-600 dark:text-gray-400">
          Akkauntingiz bormi? <Link to="/login" className="text-blue-500 font-medium">Kirish</Link>
        </p>
      </div>
    </div>
  );
};
