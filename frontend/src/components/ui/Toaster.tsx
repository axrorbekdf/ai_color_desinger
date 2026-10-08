import { useToastStore } from '../../store/useToastStore';
import { CheckCircle2, AlertCircle, Info, X } from 'lucide-react';

export const Toaster = () => {
  const { toasts, removeToast } = useToastStore();

  return (
    <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2">
      {toasts.map((toast) => {
        const icons = {
          success: <CheckCircle2 className="text-green-500" size={20} />,
          error: <AlertCircle className="text-red-500" size={20} />,
          info: <Info className="text-blue-500" size={20} />
        };
        
        const bgs = {
          success: "bg-green-50 dark:bg-green-900/30 border-green-100 dark:border-green-900/50",
          error: "bg-red-50 dark:bg-red-900/30 border-red-100 dark:border-red-900/50",
          info: "bg-blue-50 dark:bg-blue-900/30 border-blue-100 dark:border-blue-900/50"
        };
        
        const textColors = {
          success: "text-green-800 dark:text-green-200",
          error: "text-red-800 dark:text-red-200",
          info: "text-blue-800 dark:text-blue-200"
        };

        return (
          <div 
            key={toast.id}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl border shadow-sm ${bgs[toast.type]} animate-in slide-in-from-right-4 fade-in duration-300 min-w-[300px]`}
          >
            {icons[toast.type]}
            <p className={`text-sm font-medium flex-1 ${textColors[toast.type]}`}>
              {toast.message}
            </p>
            <button 
              onClick={() => removeToast(toast.id)}
              className={`p-1 rounded-md opacity-70 hover:opacity-100 transition ${textColors[toast.type]}`}
            >
              <X size={16} />
            </button>
          </div>
        );
      })}
    </div>
  );
};
