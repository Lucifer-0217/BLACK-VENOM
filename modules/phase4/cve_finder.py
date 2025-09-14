# modules/phase4/cve_finder.py
import subprocess
from datetime import datetime

def find_exploits(keyword):
    print(f"[🔎] Searching ExploitDB for: {keyword}")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_file = f"logs/phase4/exploitdb_{keyword}_{timestamp}.txt"

    try:
        result = subprocess.getoutput(f"searchsploit {keyword}")
        with open(out_file, 'w') as f:
            f.write(result)
        print(f"[✔] Saved results to: {out_file}")
    except Exception as e:
        print(f"[!] ExploitDB search failed: {e}")
