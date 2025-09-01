import requests
import json
import os
from core.utils import clean_url

def run(target):
    base_url = clean_url(target)
    print(f"[🔬] Fingerprinting {base_url} for technologies...")

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; BlackVenom/1.0; +https://github.com/Lucifer-0217)"
    }

    try:
        r = requests.get(base_url, headers=headers, timeout=5)
        server = r.headers.get("Server", "Unknown")
        powered_by = r.headers.get("X-Powered-By", "Unknown")

        tech_info = {
            "url": base_url,
            "server": server,
            "powered_by": powered_by
        }

        os.makedirs("logs/phase3", exist_ok=True)
        with open("logs/phase3/tech_fingerprint.json", "w") as f:
            json.dump(tech_info, f, indent=4)

        print("\n[✓] Technology fingerprinting complete.")
        print(f"[+] Server: {server}")
        print(f"[+] X-Powered-By: {powered_by}")
        print("[+] Results saved to logs/phase3/tech_fingerprint.json")

    except requests.exceptions.RequestException as e:
        print(f"[✘] Error connecting to {base_url}: {e}")
