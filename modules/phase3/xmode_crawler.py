import requests
import re
import os
import json
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style

COMMON_PATHS = [
    ".git/", ".env", ".DS_Store", "backup.zip", "db.sql", "config.php", "admin/", "phpmyadmin/",
    "admin.php", "login.php", "test/", "old/", "dev/", "uploads/", "core/", "backup/", "shell.php"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (XMode Recon)"
}

def crawl(target_url):
    if not target_url.startswith("http"):
        target_url = "http://" + target_url

    print(f"{Fore.CYAN}[🕷️] Crawling {target_url} for common vulnerable paths...{Style.RESET_ALL}")
    parsed_url = urlparse(target_url)
    domain = parsed_url.netloc
    found = []

    for path in COMMON_PATHS:
        full_url = urljoin(target_url, path)
        try:
            response = requests.get(full_url, headers=HEADERS, timeout=5, verify=False, allow_redirects=False)
            if response.status_code in [200, 301, 302, 403]:
                print(f"{Fore.GREEN}[+] Found: {full_url} ({response.status_code}){Style.RESET_ALL}")
                found.append({
                    "url": full_url,
                    "status": response.status_code
                })
        except requests.exceptions.RequestException:
            continue

    # Save results
    os.makedirs("logs/phase3", exist_ok=True)
    with open("logs/phase3/xmode_results.json", "w") as f:
        json.dump(found, f, indent=4)

    print(f"\n{Fore.YELLOW}[✓] XMode Scan complete. Results saved to logs/phase3/xmode_results.json{Style.RESET_ALL}")

def run(target):
    crawl(target)
