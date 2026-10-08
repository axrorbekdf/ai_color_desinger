import os
import cv2
import torch
import numpy as np
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights
from torchvision.transforms import functional as F
from abc import ABC, abstractmethod

class BaseSegmentationModel(ABC):
    @abstractmethod
    def predict(self, image_path: str):
        pass

class MaskRCNNSegmentationModel(BaseSegmentationModel):
    def __init__(self):
        # Load pre-trained model
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.weights = MaskRCNN_ResNet50_FPN_Weights.DEFAULT
        self.model = maskrcnn_resnet50_fpn(weights=self.weights, progress=False)
        self.model.to(self.device)
        self.model.eval()
        self.categories = self.weights.meta["categories"]

    def predict(self, image_path: str, confidence_threshold=0.5):
        # Read image
        img_bgr = cv2.imread(image_path)
        if img_bgr is None:
            raise ValueError(f"Could not read image at {image_path}")
        
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_tensor = F.to_tensor(img_rgb).unsqueeze(0).to(self.device)

        with torch.no_grad():
            prediction = self.model(img_tensor)[0]

        results = []
        for i in range(len(prediction['scores'])):
            score = prediction['scores'][i].item()
            if score >= confidence_threshold:
                label_idx = prediction['labels'][i].item()
                label_name = self.categories[label_idx]
                
                # Bounding box
                box = prediction['boxes'][i].cpu().numpy().tolist()
                
                # Mask
                mask = prediction['masks'][i, 0].cpu().numpy()
                mask_binary = (mask > 0.5).astype(np.uint8) * 255
                
                results.append({
                    "object_type": label_name,
                    "confidence": score,
                    "bounding_box": box,
                    "mask": mask_binary
                })
                
        return results

# Singleton instance
segmentation_model = None

def get_segmentation_model():
    global segmentation_model
    if segmentation_model is None:
        segmentation_model = MaskRCNNSegmentationModel()
    return segmentation_model
