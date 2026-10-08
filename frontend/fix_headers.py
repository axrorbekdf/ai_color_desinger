import os

def fix_header(filename):
    path = rf"d:\Projects\ai_color_desinger\frontend\src\pages\{filename}"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Remove all React and react-i18next imports from top
    new_lines = []
    i18n_added = False
    react_added = False
    
    for line in lines:
        if "react-i18next" in line or "import React" in line or "from 'react'" in line:
            pass # skip
        else:
            new_lines.append(line)
            
    # Prepend correct ones
    # read the whole to check what React hooks are needed
    content = "".join(new_lines)
    hooks = []
    if "useState" in content: hooks.append("useState")
    if "useRef" in content: hooks.append("useRef")
    if "useEffect" in content: hooks.append("useEffect")
    
    hook_str = f"import {{ {', '.join(hooks)} }} from 'react';\n" if hooks else ""
    final_content = hook_str + "import { useTranslation } from 'react-i18next';\n" + content
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(final_content)

fix_header("Upload.tsx")
fix_header("Dashboard.tsx")
fix_header("Login.tsx")
fix_header("Register.tsx")
print("Headers fixed!")
