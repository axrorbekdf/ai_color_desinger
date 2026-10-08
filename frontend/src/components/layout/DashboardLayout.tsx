import React from 'react';
import { Outlet } from 'react-router-dom';
import { Header } from './Header';
import { Sidebar } from './Sidebar';

export const DashboardLayout = () => {
  return (
    <div className="flex flex-col h-screen bg-[#f8f9fc] dark:bg-[#121212] overflow-hidden text-gray-900 dark:text-gray-100 font-sans">
      <Header />
      <div className="flex flex-1 min-h-0">
        <Sidebar />
        <main className="flex-1 overflow-auto p-6 bg-white dark:bg-[#1a1a1a] rounded-tl-2xl shadow-inner">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
