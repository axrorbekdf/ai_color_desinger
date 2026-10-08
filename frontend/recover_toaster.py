import json
import os

transcript_path = r"C:\Users\User\.gemini\antigravity\brain\fa0c67e5-54e1-49aa-8b1b-77e9c1dac57e\.system_generated\logs\transcript_full.jsonl"
recovered = None

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            entry = json.loads(line.strip())
            if "tool_calls" in entry:
                for call in entry["tool_calls"]:
                    name = call.get("name", "")
                    if "write_to_file" in name:
                        args = call.get("args", {})
                        target = args.get("TargetFile", "")
                        if target.endswith("Toaster.tsx"):
                            recovered = args.get("CodeContent")
        except Exception as e:
            pass

if recovered:
    out_path = r"d:\Projects\ai_color_desinger\frontend\src\components\ui\Toaster.tsx"
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(recovered)
    print("Recovered Toaster.tsx")
else:
    print("Could NOT find Toaster.tsx")
