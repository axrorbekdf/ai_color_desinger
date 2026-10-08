import os
import re

def clean_react_imports(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for fname in files:
            if fname.endswith(".tsx"):
                path = os.path.join(root, fname)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                content = content.replace("import React from 'react';\n", "")
                content = content.replace("import React from 'react';\r\n", "")
                content = content.replace("import React, {", "import {")
                
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

clean_react_imports(r"d:\Projects\ai_color_desinger\frontend\src")
print("Cleaned React imports safely")
