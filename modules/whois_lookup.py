# modules/whois_lookup.py

import whois
from core.utils import print_slow

def run(domain):
    print_slow(f"\n[+] Performing WHOIS lookup for {domain}...\n")
    try:
        w = whois.whois(domain)
        print(w)
    except Exception as e:
        print(f"[!] Error: {e}")
