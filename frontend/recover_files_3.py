import json

transcript_path = r"C:\Users\User\.gemini\antigravity\brain\fa0c67e5-54e1-49aa-8b1b-77e9c1dac57e\.system_generated\logs\transcript_full.jsonl"

files_to_recover = [
    "About.tsx", "AiAnalysis.tsx", "ColorRec.tsx", "DesignStyle.tsx", 
    "MoodAnalysis.tsx", "Profile.tsx", "Projects.tsx", "Results.tsx", "Settings.tsx"
]
recovered = {f: None for f in files_to_recover}

with open(transcript_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        try:
            entry = json.loads(line.strip())
            if "tool_calls" in entry:
                for call in entry["tool_calls"]:
                    name = call.get("name", "")
                    if "write_to_file" in name:
                        args = call.get("args", {}) # Wait! It's "args", not "arguments"!
                        target = args.get("TargetFile", "")
                        for fname in files_to_recover:
                            if target.endswith(fname):
                                content = args.get("CodeContent")
                                if content:
                                    recovered[fname] = content
        except Exception as e:
            if "About.tsx" in line:
                print(f"Error on line {i}: {e}")

import os
base = r"d:\Projects\ai_color_desinger\frontend\src\pages"
for fname, content in recovered.items():
    if content:
        with open(os.path.join(base, fname), "w", encoding="utf-8") as out:
            out.write(content)
        print(f"Recovered {fname}")
    else:
        print(f"Could NOT find {fname}")
