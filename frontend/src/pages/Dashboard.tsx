import { useState, useEffect } from 'react';
import { Activity, Image as ImageIcon, Sparkles, TrendingUp, Calendar, Palette, ArrowRight } from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, BarChart, Bar, Cell } from 'recharts';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';
import api from '../services/api';



export const Dashboard = () => {
  const { t } = useTranslation();
  
  const barData = [
    { name: t('dashboard.color_red'), value: 35, fill: '#ef4444' },
    { name: t('dashboard.color_blue'), value: 45, fill: '#3b82f6' },
    { name: t('dashboard.color_green'), value: 25, fill: '#22c55e' },
    { name: t('dashboard.color_yellow'), value: 20, fill: '#eab308' },
    { name: t('dashboard.color_purple'), value: 15, fill: '#a855f7' },
  ];
  
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState({
    kpis: {
      total_images: 0,
      total_objects: 0,
      total_recommendations: 0,
      avg_mood: "0%"
    },
    area_chart: [],
    recent_projects: []
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await api.get('/stats/');
        setData(res.data);
      } catch (err) {
        console.error("Failed to fetch stats", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  const stats = [
    { label: "Jami rasmlar", value: data.kpis.total_images.toString(), change: "+1", isUp: true, icon: ImageIcon, color: "text-blue-500", bg: "bg-blue-50 dark:bg-blue-900/20" },
    { label: "Aniqlangan obyektlar", value: data.kpis.total_objects.toString(), change: "+yangi", isUp: true, icon: Sparkles, color: "text-indigo-500", bg: "bg-indigo-50 dark:bg-indigo-900/20" },
    { label: "O'rtacha kayfiyat indeksi", value: data.kpis.avg_mood, change: "Zor", isUp: true, icon: Activity, color: "text-green-500", bg: "bg-green-50 dark:bg-green-900/20" },
    { label: "Tavsiya etilgan ranglar", value: data.kpis.total_recommendations.toString(), change: "+1", isUp: true, icon: Palette, color: "text-purple-500", bg: "bg-purple-50 dark:bg-purple-900/20" },
  ];

  if (loading) {
    return <div className="flex items-center justify-center h-full"><div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div></div>;
  }

  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-1">{t('dashboard.dashboard_title')}</h1>
          <p className="text-sm text-gray-500 dark:text-gray-400">{t('dashboard.dashboard_desc')}</p>
        </div>
        <Link 
          to="/upload" 
          className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-xl font-medium transition shadow-sm"
        >
          <Sparkles size={18} />
          Yangi loyiha
        </Link>
      </div>
      
      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, idx) => (
          <div key={idx} className="bg-white dark:bg-[#1a1a1a] p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 flex items-center justify-between group hover:shadow-md transition">
            <div>
              <p className="text-sm font-medium text-gray-500 dark:text-gray-400 mb-1">{stat.label}</p>
              <h3 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">{stat.value}</h3>
              <span className={`text-xs font-semibold px-2 py-1 rounded-full ${stat.isUp ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400' : 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'}`}>
                {stat.change}
              </span>
            </div>
            <div className={`p-4 rounded-xl ${stat.bg} ${stat.color} group-hover:scale-110 transition-transform`}>
              <stat.icon size={28} />
            </div>
          </div>
        ))}
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Area Chart */}
        <div className="lg:col-span-2 bg-white dark:bg-[#1a1a1a] p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-bold text-lg text-gray-900 dark:text-white flex items-center gap-2">
              <TrendingUp size={20} className="text-indigo-500" />
              Tahlil faolligi (Haftalik)
            </h3>
            <select className="bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-sm rounded-lg px-3 py-1.5 outline-none">
              <option>{t('dashboard.last_7_days')}</option>
              <option>{t('dashboard.last_30_days')}</option>
            </select>
          </div>
          <div className="h-72 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data.area_chart} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorImages" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#6366f1" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="colorObjects" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#374151" opacity={0.2} />
                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#6b7280', fontSize: 12}} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{fill: '#6b7280', fontSize: 12}} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1f2937', borderRadius: '12px', border: 'none', color: '#fff' }}
                  itemStyle={{ color: '#fff' }}
                />
                <Area type="monotone" dataKey="objects" name="Aniqlangan obyektlar" stroke="#10b981" strokeWidth={3} fillOpacity={1} fill="url(#colorObjects)" />
                <Area type="monotone" dataKey="images" name={t('dashboard.kpi_images')} stroke="#6366f1" strokeWidth={3} fillOpacity={1} fill="url(#colorImages)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Popular Colors Bar Chart */}
        <div className="lg:col-span-1 bg-white dark:bg-[#1a1a1a] p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800">
          <h3 className="font-bold text-lg text-gray-900 dark:text-white mb-6 flex items-center gap-2">
            <Palette size={20} className="text-pink-500" />
            Ommabop ranglar
          </h3>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={barData} layout="vertical" margin={{ top: 0, right: 0, left: 0, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" horizontal={true} vertical={false} stroke="#374151" opacity={0.2} />
                <XAxis type="number" hide />
                <YAxis dataKey="name" type="category" axisLine={false} tickLine={false} tick={{fill: '#6b7280', fontSize: 13}} width={70} />
                <Tooltip cursor={{fill: 'transparent'}} contentStyle={{ backgroundColor: '#1f2937', borderRadius: '8px', border: 'none', color: '#fff' }} />
                <Bar dataKey="value" radius={[0, 8, 8, 0]} barSize={20}>
                  {barData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.fill} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Recent Activity */}
      <div className="bg-white dark:bg-[#1a1a1a] rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800 overflow-hidden">
        <div className="p-6 border-b border-gray-100 dark:border-gray-800 flex items-center justify-between">
          <h3 className="font-bold text-lg text-gray-900 dark:text-white flex items-center gap-2">
            <Calendar size={20} className="text-yellow-500" />
            Oxirgi loyihalar
          </h3>
          <button className="text-sm text-indigo-600 dark:text-indigo-400 font-medium hover:underline flex items-center gap-1">
            Barchasini ko'rish <ArrowRight size={14} />
          </button>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-gray-50 dark:bg-gray-800/50 text-gray-500 dark:text-gray-400 text-sm">
                <th className="py-4 px-6 font-medium">{t('dashboard.file_name')}</th>
                <th className="py-4 px-6 font-medium">{t('dashboard.date')}</th>
                <th className="py-4 px-6 font-medium">{t('dashboard.obj_count')}</th>
                <th className="py-4 px-6 font-medium">{t('dashboard.status')}</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 dark:divide-gray-800 text-sm">
              {data.recent_projects.length > 0 ? data.recent_projects.map((row: any, idx: number) => (
                <tr key={idx} className="hover:bg-gray-50 dark:hover:bg-gray-800/50 transition">
                  <td className="py-4 px-6 font-medium text-gray-900 dark:text-white flex items-center gap-3">
                    <div className="w-8 h-8 rounded bg-gray-100 dark:bg-gray-700 flex items-center justify-center">
                      <ImageIcon size={14} className="text-gray-500" />
                    </div>
                    {row.name}
                  </td>
                  <td className="py-4 px-6 text-gray-500">{row.date}</td>
                  <td className="py-4 px-6 text-gray-500">{row.objects}</td>
                  <td className="py-4 px-6">
                    <span className={`px-2.5 py-1 rounded-full text-xs font-medium ${
                      row.status === 'Yakunlangan' 
                        ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
                        : 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400'
                    }`}>
                      {row.status}
                    </span>
                  </td>
                </tr>
              )) : (
                <tr>
                  <td colSpan={4} className="py-8 text-center text-gray-500">
                    Hali loyihalar mavjud emas. Yangi rasm yuklang!
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
