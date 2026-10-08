import os
import re

base_dir = r"d:\Projects\ai_color_desinger\frontend\src\pages"
files_to_fix = ["About.tsx", "AiAnalysis.tsx", "ColorRec.tsx", "DesignStyle.tsx", "MoodAnalysis.tsx", "Profile.tsx", "Projects.tsx", "Results.tsx", "Settings.tsx"]

for fname in files_to_fix:
    path = os.path.join(base_dir, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Strip exactly "import React from 'react';\n"
    content = content.replace("import React from 'react';\n", "")
    content = content.replace("import React, ", "import ")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Safely stripped React imports")
