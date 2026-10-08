import json
import os

transcript_path = r"C:\Users\User\.gemini\antigravity\brain\fa0c67e5-54e1-49aa-8b1b-77e9c1dac57e\.system_generated\logs\transcript_full.jsonl"

file_states = {}

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            entry = json.loads(line.strip())
            created_at = entry.get("created_at", "")
            if created_at > "2026-10-08T10:24:00Z":
                break # Stop processing once we reach the start of this session

            if "tool_calls" in entry:
                for call in entry["tool_calls"]:
                    name = call.get("name", "")
                    args = call.get("args", {})
                    
                    if "write_to_file" in name:
                        target = args.get("TargetFile", "")
                        content = args.get("CodeContent", "")
                        if target:
                            # Normalize path
                            target = target.replace("\\", "/").lower()
                            file_states[target] = content
                    
                    elif "replace_file_content" in name:
                        target = args.get("TargetFile", "")
                        if target:
                            target = target.replace("\\", "/").lower()
                            if target in file_states:
                                content = file_states[target]
                                t_c = args.get("TargetContent", "")
                                r_c = args.get("ReplacementContent", "")
                                if t_c and r_c:
                                    if t_c in content:
                                        file_states[target] = content.replace(t_c, r_c)
        except Exception as e:
            pass

# Now write out the file_states to disk
for target_lower, content in file_states.items():
    # Only recover frontend files
    if "ai_color_desinger/frontend/src" in target_lower:
        # Find the actual case-sensitive path on disk or just use a mapped path
        # Since windows is case insensitive, we can just write to the path
        # But let's reconstruct the proper path
        parts = target_lower.split("ai_color_desinger/frontend/src/")
        if len(parts) > 1:
            rel_path = parts[1]
            # fix case for known files
            rel_path = rel_path.replace("upload.tsx", "Upload.tsx")
            rel_path = rel_path.replace("projects.tsx", "Projects.tsx")
            rel_path = rel_path.replace("results.tsx", "Results.tsx")
            rel_path = rel_path.replace("dashboard.tsx", "Dashboard.tsx")
            rel_path = rel_path.replace("login.tsx", "Login.tsx")
            rel_path = rel_path.replace("register.tsx", "Register.tsx")
            rel_path = rel_path.replace("app.tsx", "App.tsx")
            rel_path = rel_path.replace("header.tsx", "Header.tsx")
            rel_path = rel_path.replace("sidebar.tsx", "Sidebar.tsx")
            rel_path = rel_path.replace("about.tsx", "About.tsx")
            rel_path = rel_path.replace("aianalysis.tsx", "AiAnalysis.tsx")
            rel_path = rel_path.replace("colorrec.tsx", "ColorRec.tsx")
            rel_path = rel_path.replace("moodanalysis.tsx", "MoodAnalysis.tsx")
            rel_path = rel_path.replace("designstyle.tsx", "DesignStyle.tsx")
            rel_path = rel_path.replace("profile.tsx", "Profile.tsx")
            rel_path = rel_path.replace("settings.tsx", "Settings.tsx")
            
            abs_path = os.path.join(r"d:\Projects\ai_color_desinger\frontend\src", rel_path)
            
            # ensure directory exists
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(abs_path, "w", encoding="utf-8") as out:
                out.write(content)
            print(f"Recovered exact state of: {rel_path}")

print("Recovery to pre-session state completed.")
