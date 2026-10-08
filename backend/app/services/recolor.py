import cv2
import numpy as np

def hex_to_bgr(hex_val: str):
    hex_val = hex_val.lstrip('#')
    return tuple(int(hex_val[i:i+2], 16) for i in (4, 2, 0)) # OpenCV uses BGR

def recolor_object(image_path: str, mask_path: str, target_hex: str, output_path: str):
    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None or mask is None:
        raise ValueError("Could not read image or mask")

    # Ensure mask is binary
    mask = (mask > 127).astype(np.uint8)

    # Convert to LAB color space to preserve lightness (L) and texture
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    
    # Target color in LAB
    target_bgr = np.uint8([[hex_to_bgr(target_hex)]])
    target_lab = cv2.cvtColor(target_bgr, cv2.COLOR_BGR2LAB)[0][0]
    
    # Extract channels
    L, a, b = cv2.split(img_lab)
    
    # We want to change the A and B channels of the masked area to the target A and B,
    # while keeping the original L channel to preserve shadows and texture.
    new_a = a.copy()
    new_b = b.copy()
    
    new_a[mask == 1] = target_lab[1]
    new_b[mask == 1] = target_lab[2]
    
    # Merge back and convert to BGR
    img_recolored_lab = cv2.merge([L, new_a, new_b])
    img_recolored = cv2.cvtColor(img_recolored_lab, cv2.COLOR_LAB2BGR)
    
    # Apply feathering to the mask for smooth blending
    mask_blurred = cv2.GaussianBlur(mask.astype(np.float32), (5, 5), 0)
    
    # Blend the original image and the recolored image using the blurred mask
    mask_3d = np.repeat(mask_blurred[:, :, np.newaxis], 3, axis=2)
    final_img = (img_recolored * mask_3d + img * (1 - mask_3d)).astype(np.uint8)
    
    cv2.imwrite(output_path, final_img)
    return True
