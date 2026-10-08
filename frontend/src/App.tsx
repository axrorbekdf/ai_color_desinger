import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { DashboardLayout } from './components/layout/DashboardLayout';
import { Dashboard } from './pages/Dashboard';
import { Upload } from './pages/Upload';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { useAuthStore } from './store/useAuthStore';

const PrivateRoute = ({ children }: { children: React.ReactNode }) => {
  const isAuthenticated = useAuthStore(state => state.isAuthenticated);
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  return <>{children}</>;
};

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        
        <Route path="/" element={<PrivateRoute><DashboardLayout /></PrivateRoute>}>
          <Route index element={<Navigate to="/upload" replace />} />
          <Route path="upload" element={<Upload />} />
          <Route path="ai-analysis" element={<Navigate to="/upload" replace />} />
          <Route path="color-rec" element={<Navigate to="/upload" replace />} />
          <Route path="mood-analysis" element={<Navigate to="/upload" replace />} />
          <Route path="design-style" element={<Navigate to="/upload" replace />} />
          <Route path="results" element={<Navigate to="/upload" replace />} />
          <Route path="recommend" element={<Navigate to="/upload" replace />} />
          <Route path="mood" element={<Navigate to="/upload" replace />} />
          <Route path="about" element={<Navigate to="/upload" replace />} />
          <Route path="projects" element={<div className="p-4">Loyihalarim (Tez orada)</div>} />
          <Route path="research" element={<div className="p-4">Tadqiqotlar (Tez orada)</div>} />
          <Route path="settings" element={<div className="p-4">Sozlamalar (Tez orada)</div>} />
          <Route path="*" element={<Navigate to="/upload" replace />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
