import { useRef, useEffect } from 'react';

interface ObjectData {
  id: number;
  object_type: string;
  confidence: number;
  bounding_box: number[]; // [x1, y1, x2, y2]
}

interface ImageCanvasProps {
  imageUrl: string;
  objects: ObjectData[];
  onSelectObject: (obj: ObjectData) => void;
  selectedObjectId?: number;
}

export const ImageCanvas: React.FC<ImageCanvasProps> = ({ imageUrl, objects, onSelectObject, selectedObjectId }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);

      // Draw bounding boxes
      objects.forEach(obj => {
        const [x1, y1, x2, y2] = obj.bounding_box;
        ctx.beginPath();
        ctx.rect(x1, y1, x2 - x1, y2 - y1);
        ctx.lineWidth = 3;
        
        if (obj.id === selectedObjectId) {
          ctx.strokeStyle = '#22c55e'; // green-500
          ctx.fillStyle = 'rgba(34, 197, 94, 0.2)';
        } else {
          ctx.strokeStyle = '#3b82f6'; // blue-500
          ctx.fillStyle = 'rgba(59, 130, 246, 0.1)';
        }
        
        ctx.fill();
        ctx.stroke();
        
        // Label
        ctx.fillStyle = obj.id === selectedObjectId ? '#22c55e' : '#3b82f6';
        ctx.fillRect(x1, y1 - 24, ctx.measureText(obj.object_type).width + 16, 24);
        ctx.fillStyle = '#ffffff';
        ctx.font = '16px Arial';
        ctx.fillText(`${obj.object_type} ${(obj.confidence*100).toFixed(0)}%`, x1 + 8, y1 - 6);
      });
    };
    img.src = imageUrl;
  }, [imageUrl, objects, selectedObjectId]);

  const handleCanvasClick = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    const x = (e.clientX - rect.left) * scaleX;
    const y = (e.clientY - rect.top) * scaleY;

    // Find clicked object (reverse order to pick top-most if overlapping)
    for (let i = objects.length - 1; i >= 0; i--) {
      const [x1, y1, x2, y2] = objects[i].bounding_box;
      if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
        onSelectObject(objects[i]);
        break;
      }
    }
  };

  return (
    <div className="relative w-full max-w-3xl mx-auto overflow-hidden rounded-xl shadow-lg border border-gray-200 dark:border-gray-800">
      <canvas 
        ref={canvasRef} 
        onClick={handleCanvasClick}
        className="w-full h-auto cursor-crosshair"
      />
    </div>
  );
};