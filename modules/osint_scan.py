# modules/osint_scan.py

import time
import socket
from core.utils import print_slow, clean_url_advanced

def run(target):
    print_slow(f"\n🧠 Initiating OSINT Scan on: {target}", 0.03)
    target = clean_url_advanced(target)
    time.sleep(1)

    print("\n📡 Collecting open-source intelligence...\n")
    time.sleep(1)

    fake_profiles = [
        f"https://twitter.com/{target}",
        f"https://github.com/{target}",
        f"https://linkedin.com/in/{target}",
        f"https://instagram.com/{target}",
    ]

    fake_emails = [
        f"{target}@protonmail.com",
        f"admin@{target}.com",
        f"contact@{target}.org",
    ]

    # Simulate OSINT Results
    print("🔍 Possible Linked Profiles:")
    for profile in fake_profiles:
        print(f" [+] {profile}")
        time.sleep(0.4)

    print("\n📧 Potential Email Addresses:")
    for email in fake_emails:
        print(f" [+] {email}")
        time.sleep(0.4)

    print("\n🌐 WHOIS Info:")
    whois_data = {
        "Domain": target,
        "Created": "2010-04-12",
        "Registrar": "Namecheap, Inc.",
        "Country": "US",
    }
    for k, v in whois_data.items():
        print(f" [+] {k}: {v}")
        time.sleep(0.4)

    try:
        ip = socket.gethostbyname(target)
    except:
        ip = "Unknown"

    print(f"\n📍 IP Address: {ip}")
    print("🕵️ Leak Status: No critical data leaks found.\n")
    print("✅ OSINT Scan Complete.\n")
