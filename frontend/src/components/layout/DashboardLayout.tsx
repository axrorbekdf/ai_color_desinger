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
        <main className="flex-1 overflow-auto p-6 bg-[#f8f9fc] dark:bg-[#0a0a0a] rounded-tl-3xl shadow-[inset_0_4px_6px_-1px_rgba(0,0,0,0.05)] dark:shadow-[inset_0_4px_6px_-1px_rgba(255,255,255,0.02)]">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
