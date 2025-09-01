# modules/subdomain_finder.py

import requests
from core.logger import log_result

def fetch_from_crtsh(domain):
    try:
        res = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=10)
        if res.status_code != 200 or not res.text.strip().startswith("["):
            raise ValueError("Invalid response or empty JSON")
        data = res.json()
        subdomains = set()
        for entry in data:
            for item in entry["name_value"].split("\n"):
                subdomains.add(item.strip())
        return subdomains
    except Exception as e:
        print(f"[⚠️] crt.sh error: {e}")
        return set()

def fetch_from_alienvault(domain):
    try:
        res = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns", timeout=10)
        if res.status_code != 200:
            raise ValueError("Invalid response from AlienVault")
        data = res.json()
        return set(entry["hostname"] for entry in data.get("passive_dns", []) if domain in entry.get("hostname", ""))
    except Exception as e:
        print(f"[⚠️] AlienVault error: {e}")
        return set()

def fetch_from_anubis(domain):
    try:
        res = requests.get(f"https://jldc.me/anubis/subdomains/{domain}", timeout=10)
        return set(res.json())
    except Exception as e:
        print(f"[⚠️] Anubis error: {e}")
        return set()

def fetch_from_hackertarget(domain):
    try:
        res = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=10)
        lines = res.text.strip().splitlines()
        return set(line.split(",")[0] for line in lines if domain in line)
    except Exception as e:
        print(f"[⚠️] HackerTarget error: {e}")
        return set()

def brute_force_subdomains(domain, wordlist_path="core/wordlists/subdomains.txt"):
    print("  🧨 Running brute-force scan...")
    found = set()
    try:
        with open(wordlist_path, "r") as f:
            for word in f:
                sub = f"{word.strip()}.{domain}"
                try:
                    res = requests.get(f"http://{sub}", timeout=3)
                    if res.status_code < 500:
                        found.add(sub)
                except:
                    continue
    except Exception as e:
        print(f"[⚠️] Brute-force error: {e}")
    return found

def run(domain):
    print(f"\n[💡] Finding subdomains for: {domain}\n")

    all_subdomains = set()

    print("  🌐 Querying crt.sh...")
    all_subdomains |= fetch_from_crtsh(domain)

    print("  🧪 Querying AlienVault OTX...")
    all_subdomains |= fetch_from_alienvault(domain)

    print("  🧠 Querying Anubis...")
    all_subdomains |= fetch_from_anubis(domain)

    print("  🕸️ Querying HackerTarget...")
    all_subdomains |= fetch_from_hackertarget(domain)

    brute = input("\n[⚙️] Do you want to run brute-force scan too? (y/n): ").strip().lower()
    if brute == "y":
        all_subdomains |= brute_force_subdomains(domain)

    # Clean & filter
    clean_subdomains = sorted({
        s.strip().lower() for s in all_subdomains
        if domain in s and " " not in s and "*" not in s
    })

    if clean_subdomains:
        print(f"\n[✅] Found {len(clean_subdomains)} unique subdomains:\n")
        for sub in clean_subdomains:
            print(f"   - {sub}")
        log_result("Subdomain Scan", f"Domain: {domain}\n" + "\n".join(clean_subdomains))
        print("\n[🔒] Result saved to logs.")
    else:
        print("[❌] No subdomains found.")

    return clean_subdomains
