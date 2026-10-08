import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { DashboardLayout } from './components/layout/DashboardLayout';
import { Dashboard } from './pages/Dashboard';
import { Upload } from './pages/Upload';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { Profile } from './pages/Profile';
import { Settings } from './pages/Settings';
import { Projects } from './pages/Projects';
import { Results } from './pages/Results';
import { About } from './pages/About';
import { AiAnalysis } from './pages/AiAnalysis';
import { ColorRec } from './pages/ColorRec';
import { MoodAnalysis } from './pages/MoodAnalysis';
import { DesignStyle } from './pages/DesignStyle';
import { useAuthStore } from './store/useAuthStore';
import { Toaster } from './components/ui/Toaster';

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
      <Toaster />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        
        <Route path="/" element={<PrivateRoute><DashboardLayout /></PrivateRoute>}>
          <Route index element={<Dashboard />} />
          <Route path="upload" element={<Upload />} />
          <Route path="profile" element={<Profile />} />
          <Route path="settings" element={<Settings />} />
          <Route path="projects" element={<Projects />} />
          <Route path="results" element={<Results />} />
          <Route path="ai-analysis" element={<AiAnalysis />} />
          <Route path="color-rec" element={<ColorRec />} />
          <Route path="mood-analysis" element={<MoodAnalysis />} />
          <Route path="design-style" element={<DesignStyle />} />
          <Route path="about" element={<About />} />
          <Route path="research" element={<div className="p-4 text-gray-900 dark:text-gray-100">Tadqiqotlar (Tez orada)</div>} />
          <Route path="*" element={<Navigate to="/upload" replace />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;