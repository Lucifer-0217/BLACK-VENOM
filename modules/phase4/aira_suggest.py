# modules/phase4/aira_suggest.py

def aira_suggest(cves):
    if not cves:
        print("[AIRA] No major CVEs found... want me to dig deeper?")
        return

    print("[🤖 AIRA] Here's my analysis of the CVEs:")
    for cve in cves:
        try:
            year = int(cve.split("-")[1])
        except Exception:
            print(f" - {cve}: ⚠️ Invalid CVE format")
            continue

        if year >= 2021:
            print(f" - {cve}: 🔥 Active and dangerous. Should check GitHub or public POCs.")
        elif 2015 <= year < 2020:
            print(f" - {cve}: ⚠️ Medium risk. Still exploitable on outdated systems.")
        else:
            print(f" - {cve}: 🧟 Legacy vuln. Check archives & old exploits.")
