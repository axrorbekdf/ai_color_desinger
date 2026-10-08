import json
import os

transcript_path = r"C:\Users\User\.gemini\antigravity\brain\fa0c67e5-54e1-49aa-8b1b-77e9c1dac57e\.system_generated\logs\transcript_full.jsonl"

def replay_replacements(filename):
    initial_content = None
    replacements = []
    
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if "tool_calls" in entry:
                    for call in entry["tool_calls"]:
                        name = call.get("name", "")
                        args = call.get("args", {})
                        target = args.get("TargetFile", "")
                        
                        if target.endswith(filename):
                            if "write_to_file" in name and not initial_content:
                                initial_content = args.get("CodeContent")
                            elif "replace_file_content" in name:
                                target_content = args.get("TargetContent", "")
                                rep_content = args.get("ReplacementContent", "")
                                if target_content and rep_content:
                                    replacements.append((target_content, rep_content))
            except Exception as e:
                pass
                
    if not initial_content: return
    content = initial_content
    for t_c, r_c in replacements:
        if t_c in content: content = content.replace(t_c, r_c)
            
    filepath = os.path.join(r"d:\Projects\ai_color_desinger\frontend\src\pages", filename)
    with open(filepath, "w", encoding="utf-8") as out:
        out.write(content)
    print(f"Replayed {len(replacements)} replacements for {filename}")

replay_replacements("Projects.tsx")
replay_replacements("Results.tsx")
