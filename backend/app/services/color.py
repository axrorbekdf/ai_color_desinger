import cv2
import numpy as np
from sklearn.cluster import MiniBatchKMeans

def get_dominant_colors(image_path: str, mask_path: str = None, n_colors: int = 5):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read image")
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    if mask_path:
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        if mask is None:
            raise ValueError("Could not read mask")
        
        # Ensure mask is binary and same size
        mask = (mask > 127).astype(np.uint8)
        
        # Apply mask
        pixels = img[mask == 1]
    else:
        pixels = img.reshape(-1, 3)

    if len(pixels) == 0:
        return []

    # Use K-Means
    kmeans = MiniBatchKMeans(n_clusters=n_colors, random_state=42, n_init=3)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    
    # Count frequencies
    counts = np.bincount(labels)
    
    # Sort colors by frequency
    sorted_idx = np.argsort(counts)[::-1]
    
    dominant_colors = []
    for idx in sorted_idx:
        color = colors[idx].tolist()
        dominant_colors.append({
            "rgb": color,
            "hex": f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}",
            "weight": float(counts[idx]) / len(pixels)
        })
        
    return dominant_colors

def rgb_to_hsv(r, g, b):
    # normalize to 0-1
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn: h = 0
    elif mx == r: h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g: h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b: h = (60 * ((r-g)/df) + 240) % 360
    s = 0 if mx == 0 else (df/mx)*100
    v = mx * 100
    return [h, s, v]

def calculate_harmony_score(color1_hsv, color2_hsv):
    h1, s1, v1 = color1_hsv
    h2, s2, v2 = color2_hsv
    
    # Calculate hue difference (shortest distance on color wheel)
    diff = abs(h1 - h2)
    hue_dist = min(diff, 360 - diff)
    
    # Check standard harmonies
    harmonies = {
        "monochromatic": abs(hue_dist) <= 15,
        "analogous": abs(hue_dist - 30) <= 15,
        "complementary": abs(hue_dist - 180) <= 15,
        "split_complementary": abs(hue_dist - 150) <= 15 or abs(hue_dist - 210) <= 15,
        "triadic": abs(hue_dist - 120) <= 15,
    }
    
    # Score 0-100 based on how close it is to a perfect harmony
    # For a thesis, we can define a deterministic function:
    # Max score if it hits one of the sweet spots exactly.
    distances_to_perfect = [
        abs(hue_dist),          # mono
        abs(hue_dist - 30),     # analogous
        abs(hue_dist - 180),    # complementary
        abs(hue_dist - 150),    # split 1
        abs(hue_dist - 120),    # triadic
    ]
    min_dist = min(distances_to_perfect)
    
    # 0 distance = 100 score, 90 distance (worst possible) = 0 score
    score = max(0, 100 - (min_dist / 90.0) * 100)
    
    return score
