from app.services.color import rgb_to_hsv, calculate_harmony_score

# Predefined standard colors for recommendation (for thesis POC)
# A real implementation would have a large dataset of named colors
STANDARD_COLORS = [
    {"name": "Sage Green", "rgb": [113, 133, 104]},
    {"name": "Terracotta", "rgb": [226, 114, 91]},
    {"name": "Navy Blue", "rgb": [0, 0, 128]},
    {"name": "Mustard Yellow", "rgb": [255, 219, 88]},
    {"name": "Dusty Rose", "rgb": [220, 164, 168]},
    {"name": "Charcoal", "rgb": [54, 69, 79]},
    {"name": "Cream", "rgb": [255, 253, 208]},
    {"name": "Teal", "rgb": [0, 128, 128]},
]

def generate_recommendations(env_colors, design_style: str, mood_goal: str, n_recommendations: int = 5):
    # Compute environment average hue to find harmony
    env_hsv_list = [rgb_to_hsv(*c["rgb"]) for c in env_colors]
    avg_env_h = sum(c[0] for c in env_hsv_list) / len(env_hsv_list) if env_hsv_list else 0
    avg_env_s = sum(c[1] for c in env_hsv_list) / len(env_hsv_list) if env_hsv_list else 0
    avg_env_v = sum(c[2] for c in env_hsv_list) / len(env_hsv_list) if env_hsv_list else 0
    
    avg_env_hsv = [avg_env_h, avg_env_s, avg_env_v]

    recommendations = []
    
    for color in STANDARD_COLORS:
        c_hsv = rgb_to_hsv(*color["rgb"])
        
        # 1. Harmony Score (0-100)
        harmony_score = calculate_harmony_score(avg_env_hsv, c_hsv)
        
        # 2. Mood Score (0-100)
        # Simplified deterministic logic for thesis based on Color Psychology
        mood_score = 50
        if mood_goal == "Calm":
            if c_hsv[0] >= 90 and c_hsv[0] <= 240: # Greens to Blues
                mood_score = 90
            elif c_hsv[1] < 30: # Low saturation neutrals
                mood_score = 80
                
        elif mood_goal == "Energetic":
            if c_hsv[0] < 60 or c_hsv[0] > 300: # Reds, Oranges
                mood_score = 95
            if c_hsv[1] > 70: # High saturation
                mood_score = min(100, mood_score + 10)
        
        # 3. Style Match (0-100)
        style_score = 50
        if design_style == "Minimalist":
            if c_hsv[1] < 20 or c_hsv[2] > 90 or c_hsv[2] < 20: # Whites, Blacks, Grays
                style_score = 90
        elif design_style == "Natural":
            if (c_hsv[0] >= 60 and c_hsv[0] <= 150) or (c_hsv[0] >= 20 and c_hsv[0] <= 50 and c_hsv[1] < 50):
                # Greens and earthy tones
                style_score = 95
                
        overall_score = (harmony_score * 0.4) + (mood_score * 0.4) + (style_score * 0.2)
        
        recommendations.append({
            "color_name": color["name"],
            "rgb_val": color["rgb"],
            "hex_val": f"#{color['rgb'][0]:02x}{color['rgb'][1]:02x}{color['rgb'][2]:02x}",
            "hsv_val": c_hsv,
            "harmony_score": round(harmony_score, 2),
            "mood_score": round(mood_score, 2),
            "compatibility_score": round(overall_score, 2),
            "recommendation_reason": f"Chosen for its {mood_score}% match with {mood_goal} mood and {harmony_score}% harmony with surroundings."
        })
        
    # Sort by overall compatibility
    recommendations.sort(key=lambda x: x["compatibility_score"], reverse=True)
    return recommendations[:n_recommendations]
