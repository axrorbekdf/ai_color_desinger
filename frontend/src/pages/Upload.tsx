import React, { useState, useRef } from 'react';
import { UploadCloud, CheckCircle2, SlidersHorizontal, Image as ImageIcon, Sparkles, Hand, ZoomIn, RotateCcw, Plus, Loader2, Layers, Smile, ChevronDown, MousePointer2 } from 'lucide-react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts';
import api from '../services/api';

export const Upload = () => {
  const [activeTab, setActiveTab] = useState('detect');
  
  const [isLoading, setIsLoading] = useState(false);
  const [loadingText, setLoadingText] = useState('');
  const [projectId, setProjectId] = useState<number | null>(null);
  const [imageUrl, setImageUrl] = useState<string | null>(null);
  const [objects, setObjects] = useState<any[]>([]);
  const [selectedObj, setSelectedObj] = useState<any | null>(null);
  const [recommendations, setRecommendations] = useState<any[]>([]);
  const [selectedRecIndex, setSelectedRecIndex] = useState<number>(0);
  const [recoloredUrl, setRecoloredUrl] = useState<string | null>(null);

  // Pan and Zoom states
  const [zoom, setZoom] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });
  const [activeTool, setActiveTool] = useState('pointer'); // pointer, hand, zoom
  const [isDragging, setIsDragging] = useState(false);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsLoading(true);
    try {
      setLoadingText('Loyiha yaratilmoqda...');
      const projRes = await api.post('/projects/', { name: "Yangi Loyiha", design_style: "Modern", mood_goal: "Calm" });
      const pid = projRes.data.id;
      setProjectId(pid);

      setLoadingText('Rasm yuklanmoqda...');
      const formData = new FormData();
      formData.append('file', file);
      await api.post(`/images/upload?project_id=${pid}`, formData);
      setImageUrl(URL.createObjectURL(file));

      setLoadingText('AI obyektlarni aniqlamoqda...');
      const segRes = await api.post(`/analysis/segment/${pid}`);
      setObjects(segRes.data.objects);
      
    } catch (error) {
      console.error(error);
      alert('Xatolik yuz berdi!');
    } finally {
      setIsLoading(false);
    }
  };

  const handleObjectSelect = async (obj: any) => {
    setSelectedObj(obj);
    if (!projectId) return;
    
    setIsLoading(true);
    setLoadingText('Ranglar tahlil qilinmoqda...');
    try {
      const recRes = await api.post(`/colors/recommend/${projectId}`, { object_id: obj.id });
      setRecommendations(recRes.data.recommendations || []);
      setSelectedRecIndex(0);
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleMouseDown = (e: React.MouseEvent) => {
    if (activeTool === 'hand') {
      setIsDragging(true);
    } else if (activeTool === 'zoom') {
      setZoom(z => Math.min(z + 0.5, 4));
    }
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (isDragging && activeTool === 'hand') {
      setPan(p => ({ x: p.x + e.movementX, y: p.y + e.movementY }));
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const resetView = () => {
    setZoom(1);
    setPan({ x: 0, y: 0 });
    setActiveTool('pointer');
  };

  const applyColor = async () => {
    if (!projectId || recommendations.length === 0) return;
    const recId = recommendations[selectedRecIndex].id;
    
    setIsLoading(true);
    setLoadingText("Rang qo'llanilmoqda...");
    try {
      const colRes = await api.post(`/recolor/${projectId}`, { recommendation_id: recId });
      const path = colRes.data.modified_image_path;
      const relativePath = path.replace('../storage/', '');
      const fullUrl = import.meta.env.VITE_API_URL.replace('/api/v1', '') + '/storage/' + relativePath;
      setRecoloredUrl(fullUrl);
    } catch (err) {
      console.error(err);
      alert("Rang qo'llashda xatolik yuz berdi");
    } finally {
      setIsLoading(false);
    }
  };

  const getColorForObject = (type: string) => {
    const t = type.toLowerCase();
    if (t.includes('couch') || t.includes('sofa') || t.includes('bed')) return { bg: 'bg-blue-500', border: 'border-blue-500', name: 'Divan' };
    if (t.includes('wall') || t.includes('devor')) return { bg: 'bg-green-500', border: 'border-green-500', name: 'Devor' };
    if (t.includes('curtain') || t.includes('parda') || t.includes('window')) return { bg: 'bg-purple-500', border: 'border-purple-500', name: 'Parda' };
    if (t.includes('table') || t.includes('stol')) return { bg: 'bg-orange-500', border: 'border-orange-500', name: 'Stol' };
    if (t.includes('rug') || t.includes('carpet') || t.includes('gilam') || t.includes('floor')) return { bg: 'bg-yellow-500', border: 'border-yellow-500', name: 'Gilam' };
    if (t.includes('plant') || t.includes('flower')) return { bg: 'bg-emerald-600', border: 'border-emerald-600', name: 'O\'simlik' };
    return { bg: 'bg-indigo-500', border: 'border-indigo-500', name: type };
  };

  const pieData = [
    { name: 'Xotirjamlik', value: 78, color: '#22c55e' },
    { name: 'Quvonch', value: 12, color: '#0ea5e9' },
    { name: 'Ishonch', value: 6, color: '#eab308' },
    { name: 'Stress', value: 3, color: '#f97316' },
    { name: 'Tushkunlik', value: 1, color: '#ef4444' },
  ];

  return (
    <div className="flex gap-6 h-full text-sm relative">
      {isLoading && (
        <div className="absolute inset-0 z-50 bg-white/70 backdrop-blur-sm flex flex-col items-center justify-center rounded-2xl">
          <Loader2 className="animate-spin text-indigo-600 mb-4" size={40} />
          <h2 className="text-xl font-bold text-gray-800">{loadingText}</h2>
        </div>
      )}

      {/* LEFT COLUMN */}
      <div className="flex-1 flex flex-col gap-6 w-[55%]">
        
        {/* TABS & IMAGE VIEWER */}
        <div className="bg-white p-4 rounded-2xl shadow-sm border border-gray-100 flex-1 flex flex-col">
          <div className="flex gap-3 mb-4">
            <button className={`flex items-center gap-2 px-4 py-2 rounded-lg font-bold transition text-xs ${activeTab === 'detect' ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}`} onClick={() => setActiveTab('detect')}>
              <ImageIcon size={16} /> Obyektlarni aniqlash
            </button>
            <button className={`flex items-center gap-2 px-4 py-2 rounded-lg font-bold transition text-xs ${activeTab === 'auto' ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}`} onClick={() => setActiveTab('auto')}>
              <Sparkles size={16} /> Rangni avtomatik tanlash
            </button>
            <button className={`flex items-center gap-2 px-4 py-2 rounded-lg font-bold transition text-xs ${activeTab === 'mood' ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}`} onClick={() => setActiveTab('mood')}>
              <SlidersHorizontal size={16} /> Kayfiyatga moslashtirish
            </button>
          </div>
          
          <div className="relative flex-1 bg-gray-50 rounded-xl overflow-hidden border border-gray-200 flex items-center justify-center h-[420px]">
            {!imageUrl ? (
              <div className="text-center">
                <input type="file" className="hidden" id="upload-btn" accept="image/*" onChange={handleFileUpload} />
                <label htmlFor="upload-btn" className="cursor-pointer bg-indigo-600 text-white px-6 py-3 rounded-lg font-bold shadow-md hover:bg-indigo-700 transition flex items-center gap-2">
                  <UploadCloud size={20} /> Rasmni yuklang
                </label>
              </div>
            ) : (
              <div 
                className={`relative w-full h-full flex items-center justify-center ${activeTool === 'hand' ? (isDragging ? 'cursor-grabbing' : 'cursor-grab') : activeTool === 'zoom' ? 'cursor-zoom-in' : ''}`}
                onMouseDown={handleMouseDown}
                onMouseMove={handleMouseMove}
                onMouseUp={handleMouseUp}
                onMouseLeave={handleMouseUp}
              >
                <div 
                  className="relative transition-transform duration-75 max-w-full max-h-full flex items-center justify-center"
                  style={{ transform: `translate(${pan.x}px, ${pan.y}px) scale(${zoom})`, transformOrigin: 'center' }}
                >
                  <div className="relative inline-block">
                    <img 
                      src={imageUrl} 
                      alt="Uploaded" 
                      className="rounded-xl select-none" 
                      style={{ maxHeight: '400px', maxWidth: '100%', objectFit: 'contain' }}
                      draggable={false}
                      onLoad={(e) => {
                         const target = e.target as HTMLImageElement;
                         target.setAttribute('data-w', target.naturalWidth.toString());
                         target.setAttribute('data-h', target.naturalHeight.toString());
                      }} 
                    />
                    
                    {/* Dynamic Bounding Boxes */}
                  {objects.map((obj) => {
                    const [x1, y1, x2, y2] = obj.bounding_box;
                    const style = getColorForObject(obj.object_type);
                    const isSelected = selectedObj?.id === obj.id;
                    
                    return (
                      <div 
                        key={obj.id}
                        onClick={(e) => {
                          if (activeTool === 'pointer') {
                            e.stopPropagation();
                            handleObjectSelect(obj);
                          }
                        }}
                        className={`absolute border-2 transition-all ${activeTool === 'pointer' ? 'cursor-pointer' : ''} ${isSelected ? `${style.border} bg-white/20 z-10 shadow-[0_0_15px_rgba(255,255,255,0.5)]` : `${style.border} hover:bg-white/10`}`}
                        style={{ 
                          left: `${(x1/1000)*100}%`,
                          top: `${(y1/1000)*100}%`,
                          width: `${((x2-x1)/1000)*100}%`,
                          height: `${((y2-y1)/1000)*100}%`,
                        }}
                      >
                        {/* Box Handle dots for selected state */}
                        {isSelected && (
                           <>
                             <div className="absolute -top-1 -left-1 w-2 h-2 bg-white border border-gray-400"></div>
                             <div className="absolute -top-1 -right-1 w-2 h-2 bg-white border border-gray-400"></div>
                             <div className="absolute -bottom-1 -left-1 w-2 h-2 bg-white border border-gray-400"></div>
                             <div className="absolute -bottom-1 -right-1 w-2 h-2 bg-white border border-gray-400"></div>
                           </>
                        )}
                        <span className={`absolute -top-7 left-1/2 -translate-x-1/2 text-white px-3 py-1 rounded-md text-xs font-bold whitespace-nowrap shadow-md ${style.bg}`}>
                          {style.name}
                        </span>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Floating Toolbar inside image */}
            {imageUrl && (
              <div className="absolute top-4 right-4 bg-white p-1.5 rounded-xl shadow-lg flex flex-col gap-2 z-20">
                <button onClick={() => setActiveTool('pointer')} className={`p-2 rounded-lg transition ${activeTool === 'pointer' ? 'bg-indigo-100 text-indigo-700' : 'hover:bg-gray-100 text-gray-600'}`}><MousePointer2 size={18} /></button>
                <button onClick={() => setActiveTool('hand')} className={`p-2 rounded-lg transition ${activeTool === 'hand' ? 'bg-indigo-100 text-indigo-700' : 'hover:bg-gray-100 text-gray-600'}`}><Hand size={18} /></button>
                <button onClick={() => setActiveTool('zoom')} className={`p-2 rounded-lg transition ${activeTool === 'zoom' ? 'bg-indigo-100 text-indigo-700' : 'hover:bg-gray-100 text-gray-600'}`}><ZoomIn size={18} /></button>
                <button onClick={resetView} className="p-2 hover:bg-gray-100 rounded-lg text-gray-600 transition"><RotateCcw size={18} /></button>
              </div>
            )}
          </div>
        </div>

        {/* BEFORE AFTER */}
        <div className="bg-white p-4 rounded-2xl shadow-sm border border-gray-100">
          <h3 className="font-bold flex items-center gap-2 mb-3 text-sm">
            <span className="bg-indigo-600 text-white w-5 h-5 rounded-full flex items-center justify-center text-[10px]">3</span> 
            Natija (Before / After)
          </h3>
          <div className="relative w-full aspect-[21/9] rounded-xl overflow-hidden flex shadow-sm border border-gray-200">
             <div className="flex-1 relative border-r border-white">
                {imageUrl ? <img src={imageUrl} className="object-cover w-full h-full" alt="Original" /> : <div className="w-full h-full bg-gray-100 flex items-center justify-center"><ImageIcon className="text-gray-300" size={32}/></div>}
                <span className="absolute top-3 left-3 bg-gray-900/80 text-white text-[11px] font-medium px-3 py-1 rounded-full shadow-sm">Original</span>
             </div>
             <div className="flex-1 relative">
                {recoloredUrl ? <img src={recoloredUrl} className="object-cover w-full h-full" alt="Recolored" /> : (imageUrl ? <img src={imageUrl} className="object-cover w-full h-full filter sepia hue-rotate-90 opacity-80" alt="Recolored Fake" /> : <div className="w-full h-full bg-gray-100 flex items-center justify-center"><ImageIcon className="text-gray-300" size={32}/></div>)}
                <span className="absolute top-3 left-3 bg-gray-900/80 text-white text-[11px] font-medium px-3 py-1 rounded-full shadow-sm">AI rang qo'llangan</span>
             </div>
             
             {/* Slider Handle in middle */}
             <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 bg-white rounded-full shadow-lg flex items-center justify-center text-gray-600 font-bold text-[10px] cursor-ew-resize border border-gray-100 z-10">
               &lt; &gt;
             </div>
          </div>
        </div>
      </div>

      {/* RIGHT COLUMN */}
      <div className="flex-1 flex flex-col gap-6 w-[45%]">
        
        {/* TOP CONTROLS */}
        <div className="grid grid-cols-2 gap-4">
          <div className="col-span-1 bg-white p-4 rounded-2xl shadow-sm border border-gray-100">
            <h3 className="font-bold flex items-center gap-2 mb-3 text-sm">
              <span className="bg-indigo-600 text-white w-5 h-5 rounded-full flex items-center justify-center text-[10px]">1</span> 
              Tanlangan obyekt: {selectedObj ? getColorForObject(selectedObj.object_type).name : 'Divan'}
            </h3>
            <div className="border border-gray-200 rounded-xl p-1.5 flex items-center justify-between bg-white shadow-sm cursor-pointer hover:border-indigo-300 transition">
              <div className="flex items-center gap-3">
                <div className="w-12 h-8 bg-indigo-100 rounded overflow-hidden flex items-center justify-center">
                   {imageUrl ? <img src={imageUrl} className="w-full h-full object-cover" /> : <ImageIcon size={14} className="text-indigo-300"/>}
                </div>
                <span className="font-semibold text-[13px] text-gray-700">{selectedObj ? getColorForObject(selectedObj.object_type).name : 'Divan'}</span>
              </div>
              <ChevronDown size={16} className="text-gray-400 mr-1" />
            </div>
          </div>
          
          <div className="col-span-1 flex flex-col gap-3">
            <div className="bg-white p-3 rounded-2xl shadow-sm border border-gray-100">
               <h3 className="font-bold flex items-center gap-2 mb-2 text-xs"><Layers size={14} className="text-indigo-600" /> Dizayn uslubi</h3>
               <div className="border border-gray-200 rounded-lg px-3 py-1.5 flex items-center justify-between bg-white cursor-pointer">
                 <span className="text-xs font-medium text-gray-700">Minimalist</span>
                 <ChevronDown size={14} className="text-gray-400" />
               </div>
            </div>
            <div className="bg-white p-3 rounded-2xl shadow-sm border border-gray-100">
               <h3 className="font-bold flex items-center gap-2 mb-2 text-xs"><Smile size={14} className="text-indigo-600" /> Maqsad / Kayfiyat</h3>
               <div className="border border-gray-200 rounded-lg px-3 py-1.5 flex items-center justify-between bg-white cursor-pointer">
                 <span className="text-xs font-medium text-gray-700">Xotirjam va muvozanatli</span>
                 <ChevronDown size={14} className="text-gray-400" />
               </div>
            </div>
          </div>
        </div>

        {/* AI RECOMMENDATIONS */}
        <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-100">
           <h3 className="font-bold flex items-center gap-2 mb-4 text-sm">
             <span className="bg-indigo-600 text-white w-5 h-5 rounded-full flex items-center justify-center text-[10px]">2</span> 
             AI rang tavsiyalari <span className="text-gray-400 font-normal ml-1 text-xs">(Dizayn va kayfiyat asosida)</span>
           </h3>
           <div className="grid grid-cols-4 gap-3">
              {recommendations.length > 0 ? recommendations.map((rec, i) => (
                <div key={rec.id} onClick={() => setSelectedRecIndex(i)} className={`border rounded-xl p-2.5 cursor-pointer transition ${selectedRecIndex === i ? 'border-indigo-600 shadow-md ring-1 ring-indigo-600 bg-indigo-50/10' : 'border-gray-200 hover:border-indigo-300 hover:shadow-sm'}`}>
                   <div className="relative h-20 rounded-lg mb-2 overflow-hidden bg-gray-100 border border-black/5" style={{ backgroundColor: rec.hex_val }}>
                     {imageUrl && <img src={imageUrl} className="w-full h-full object-cover opacity-50 mix-blend-overlay" />}
                     {selectedRecIndex === i && <div className="absolute top-1 right-1 bg-indigo-600 text-white rounded-full w-5 h-5 flex items-center justify-center shadow-sm"><CheckCircle2 size={12} strokeWidth={3} /></div>}
                   </div>
                   <p className="font-semibold text-[11px] leading-tight mb-1 text-gray-800">{rec.color_name}</p>
                   <p className="font-bold text-[13px] text-gray-900 mb-2">{rec.compatibility_score}% mos</p>
                   <div className="flex gap-1.5">
                      <div className="w-4 h-4 rounded-full" style={{backgroundColor: rec.hex_val}}></div>
                      <div className="w-4 h-4 rounded-full opacity-70" style={{backgroundColor: rec.hex_val}}></div>
                      <div className="w-4 h-4 rounded-full opacity-40" style={{backgroundColor: rec.hex_val}}></div>
                      <div className="w-4 h-4 rounded-full opacity-20" style={{backgroundColor: rec.hex_val}}></div>
                   </div>
                </div>
              )) : (
                 // Dummy cards matching mockup if no data yet
                 [
                  { name: "Tabiiy va xotirjam", match: 92, active: true, colors: ['#698263', '#839E7C', '#C2D1BC', '#EEF2EC'] },
                  { name: "Zamonaviy va ishonchli", match: 87, active: false, colors: ['#44719C', '#618CBA', '#A4BFDB', '#E0EBF5'] },
                  { name: "Yorqin va ijobiy", match: 81, active: false, colors: ['#D2AD7B', '#E3C69D', '#F0E2CD', '#FAF6F2'] },
                  { name: "Energiya va ishtiyoq", match: 76, active: false, colors: ['#CC5555', '#E67A7A', '#F2B6B6', '#FAEEEE'] }
                ].map((item, i) => (
                  <div key={i} className={`border rounded-xl p-2.5 cursor-pointer transition ${item.active ? 'border-indigo-600 shadow-md ring-1 ring-indigo-600 bg-indigo-50/10' : 'border-gray-200 hover:border-indigo-300 hover:shadow-sm'}`}>
                     <div className="relative h-20 rounded-lg mb-2 overflow-hidden bg-gray-100" style={{ backgroundColor: item.colors[0] }}>
                       {imageUrl && <img src={imageUrl} className="w-full h-full object-cover opacity-50 mix-blend-overlay" />}
                       {item.active && <div className="absolute top-1 right-1 bg-indigo-600 text-white rounded-full w-5 h-5 flex items-center justify-center shadow-sm"><CheckCircle2 size={12} strokeWidth={3} /></div>}
                     </div>
                     <p className="font-semibold text-[11px] leading-tight mb-1 text-gray-800">{item.name}</p>
                     <p className="font-bold text-[13px] text-gray-900 mb-2">{item.match}% mos</p>
                     <div className="flex gap-1.5">
                        {item.colors.map((c, j) => (
                          <div key={j} className="w-4 h-4 rounded-full border border-black/5" style={{ backgroundColor: c }}></div>
                        ))}
                     </div>
                  </div>
                ))
              )}
           </div>
           
           <div className="flex gap-3 mt-5">
              <button onClick={applyColor} disabled={recommendations.length === 0 && !imageUrl} className="flex-[2] bg-indigo-600 hover:bg-indigo-700 disabled:bg-indigo-300 disabled:cursor-not-allowed text-white rounded-xl py-3 font-semibold flex justify-center items-center gap-2 transition shadow-md shadow-indigo-200">
                 <CheckCircle2 size={18} /> Bu rangni qo'llash
              </button>
              <button className="flex-1 bg-white border border-gray-200 hover:bg-gray-50 text-indigo-600 rounded-xl py-3 font-semibold flex justify-center items-center gap-2 transition">
                 <RotateCcw size={16} /> Boshqa variantlar
              </button>
              <button className="flex-1 bg-white border border-gray-200 hover:bg-gray-50 text-indigo-600 rounded-xl py-3 font-semibold flex justify-center items-center gap-2 transition">
                 <Plus size={16} /> Palitrani saqlash
              </button>
           </div>
        </div>

        {/* ANALYSIS BOTTOM ROW */}
        <div className="flex gap-4 flex-1">
           <div className="flex-1 bg-white p-5 rounded-2xl shadow-sm border border-gray-100">
              <div className="flex justify-between items-center mb-4">
                <h3 className="font-bold flex items-center gap-2 text-sm">
                  <span className="bg-indigo-600 text-white w-5 h-5 rounded-full flex items-center justify-center text-[10px]">4</span> 
                  Tanlangan rang palitrasi
                </h3>
              </div>
              <div className="flex items-center gap-2 mb-6 border-b pb-5">
                <div className="w-12 h-12 rounded-lg bg-[#698263] shadow-inner"></div>
                <div className="w-10 h-10 rounded-full bg-[#839E7C]"></div>
                <div className="w-10 h-10 rounded-full bg-[#C2D1BC]"></div>
                <div className="w-10 h-10 rounded-full bg-[#EEF2EC]"></div>
                <button className="w-10 h-10 rounded-full border-2 border-dashed border-gray-300 flex items-center justify-center text-gray-400 hover:bg-gray-50 hover:text-gray-600 transition ml-1"><Plus size={18}/></button>
              </div>
              
              <h4 className="font-bold mb-4 text-xs text-gray-800">Rang ma'nosi va psixologik ta'siri</h4>
              <div className="flex gap-5 items-center">
                 <div className="w-14 h-32 bg-[#698263] rounded-lg shadow-inner"></div>
                 <div className="flex-1 space-y-3">
                    {[
                      { l: 'Xotirjamlik', v: 85 },
                      { l: 'Muvozanat', v: 78 },
                      { l: 'Ishonch', v: 62 },
                      { l: 'Stress kamayishi', v: 71 },
                      { l: 'Diqqat', v: 68 },
                    ].map((st, i) => (
                      <div key={i} className="flex items-center gap-3 text-[11px]">
                         <span className="w-24 font-medium text-gray-600">{st.l}</span>
                         <div className="flex-1 h-2 bg-gray-100 rounded-full overflow-hidden">
                           <div className="h-full bg-[#698263] rounded-full" style={{ width: `${st.v}%`}}></div>
                         </div>
                         <span className="font-bold w-6 text-right text-gray-700">{st.v}%</span>
                      </div>
                    ))}
                 </div>
              </div>
              <p className="text-[11px] text-gray-500 mt-4 leading-relaxed font-medium">
                Yashil rang tabiat, tinchlik va muvozanat bilan bog'liq. U stressni kamaytiradi, ruhiy holatni yaxshilaydi va diqqatni jamlashga yordam beradi.
              </p>
           </div>
           
           <div className="flex-[0.9] bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col">
              <h3 className="font-bold flex items-center gap-2 mb-4 text-sm">
                <span className="bg-indigo-600 text-white w-5 h-5 rounded-full flex items-center justify-center text-[10px]">5</span> 
                Rang va kayfiyat tahlili
              </h3>
              
              <div className="flex-1 flex flex-col justify-center">
                 <div className="flex items-center gap-4 mb-2">
                   <div className="w-[120px] h-[120px] relative">
                      <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                          <Pie data={pieData} innerRadius={35} outerRadius={55} paddingAngle={2} dataKey="value" stroke="none">
                            {pieData.map((entry, index) => (
                              <Cell key={`cell-${index}`} fill={entry.color} />
                            ))}
                          </Pie>
                          <Tooltip />
                        </PieChart>
                      </ResponsiveContainer>
                      <div className="absolute inset-0 flex flex-col items-center justify-center">
                         <Smile size={18} className="text-green-500 mb-0.5" />
                         <span className="text-[9px] font-bold text-center leading-tight text-gray-600">Umumiy kayfiyat<br/><span className="text-gray-900 text-[11px]">78%</span></span>
                      </div>
                   </div>
                   <div className="flex-1 flex flex-col gap-2.5 text-[11px]">
                      {pieData.map(d => (
                         <div key={d.name} className="flex justify-between items-center">
                           <span className="flex items-center gap-2 font-medium text-gray-600"><div className="w-2.5 h-2.5 rounded-full" style={{backgroundColor: d.color}}></div> {d.name}</span>
                           <span className="font-bold text-gray-800">{d.value}%</span>
                         </div>
                      ))}
                   </div>
                 </div>
              </div>

              <div className="bg-green-50/50 border border-green-100 p-3.5 rounded-xl mt-3">
                 <h4 className="font-bold text-green-700 text-xs flex items-center gap-1.5 mb-1.5"><Sparkles size={14} /> Xulosa</h4>
                 <p className="text-[11px] text-green-800/80 leading-relaxed font-medium">
                   Tanlangan ranglar palitrasi sizda asosan <strong className="text-green-800">xotirjamlik</strong> va <strong className="text-green-800">ijobiy kayfiyatni</strong> aks ettiradi. Bu palitra dam olish uchun mos.
                 </p>
              </div>
           </div>
        </div>

      </div>
    </div>
  );
};
