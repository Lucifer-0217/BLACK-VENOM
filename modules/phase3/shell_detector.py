import requests
import re
import os
import json
import urllib3
from urllib.parse import urljoin
from core.utils import clean_url
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

def run(target):
    base_url = clean_url(target)
    print(f"\n[🐚] Scanning {base_url} for suspicious web shell files...")

    shell_signatures = [
        r"c99", r"r57", r"cmd", r"webshell", r"upload", r"backdoor",
        r"eval\(", r"base64_decode", r"system\(", r"shell_exec\(",
        r"passthru\(", r"preg_replace\(.*/e", r"exec\("
    ]

    common_paths = [
        "c99.php", "r57.php", "cmd.php", "shell.php", "upload.php",
        "backdoor.php", "evil.php", "adminer.php", "test.php",
        ".git/config", ".htaccess", ".env"
    ]

    findings = []

    for path in common_paths:
        full_url = urljoin(base_url, path)
        try:
            response = requests.get(full_url, verify=False, timeout=5)
            if response.status_code == 200:
                for pattern in shell_signatures:
                    if re.search(pattern, response.text, re.IGNORECASE):
                        print(f"[⚠️] Suspicious file found: {full_url} → Pattern matched: `{pattern}`")
                        findings.append({
                            "url": full_url,
                            "pattern": pattern
                        })
                        break
        except requests.exceptions.RequestException:
            continue

    os.makedirs("logs/phase3", exist_ok=True)
    with open("logs/phase3/shell_detector.json", "w") as f:
        json.dump(findings, f, indent=4)

    print("\n[✓] Shell detection complete.")
    if findings:
        print(f"[+] {len(findings)} suspicious file(s) found. Saved to logs/phase3/shell_detector.json\n")
    else:
        print("[-] No suspicious shell patterns found.\n")
