# modules/cursed_recon.py

import requests
import os
from urllib.parse import urlparse
from modules.header_grabber import grab_headers

def cursed_paths_enum(target):
    print(f"\n[🔮] Starting cursed recon on: {target}")
    paths = ['admin', 'login', 'dashboard', 'config', '.git', '.env', 'server-status']
    found = []

    for path in paths:
        url = target.rstrip('/') + '/' + path
        try:
            r = requests.get(url, timeout=5)
            if r.status_code in [200, 403]:
                print(f"[👁️‍🗨️] Found: {url} [Status: {r.status_code}]")
                found.append(url)
        except requests.RequestException:
            continue

    if not found:
        print("[👻] No cursed paths found.")
    else:
        log_path = "logs/cursed_paths.txt"
        with open(log_path, "a") as log:
            for f in found:
                log.write(f + "\n")
        print(f"[🔒] Cursed recon results saved to {log_path}")

def run(target):
    parsed = urlparse(target)
    domain = parsed.netloc if parsed.netloc else parsed.path
    if not domain.startswith("http"):
        domain = "http://" + domain

    # Reuse the header grabber inside cursed recon
    print(f"\n[🧠] Running header grabber from cursed mode...")
    grab_headers(domain)
    
    # Run cursed paths enumeration
    cursed_paths_enum(domain)
