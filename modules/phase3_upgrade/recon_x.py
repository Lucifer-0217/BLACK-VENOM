import requests
from bs4 import BeautifulSoup
import socket

def recon_x():
    print("\n🔬 RECON-X: Advanced Recon Tool (Phase 3-UPGRADE)")

    domain = input("🔗 Enter domain or target: ").strip()

    if not domain:
        print("❌ Invalid input.")
        return

    if not domain.startswith("http"):
        url = "http://" + domain
    else:
        url = domain

    print("\n⏳ Starting advanced recon on:", url)

    # Step 1: WHOIS Lookup (Basic)
    try:
        print("\n📄 WHOIS Lookup:")
        response = requests.get(f"https://api.hackertarget.com/whois/?q={domain}")
        print(response.text)
    except Exception as e:
        print("⚠️ WHOIS failed:", e)

    # Step 2: DNS Lookup
    try:
        print("\n🌐 DNS Records:")
        response = requests.get(f"https://api.hackertarget.com/dnslookup/?q={domain}")
        print(response.text)
    except Exception as e:
        print("⚠️ DNS Lookup failed:", e)

    # Step 3: IP Address & Geolocation
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n🌍 Resolved IP: {ip}")

        geo_res = requests.get(f"http://ip-api.com/json/{ip}")
        geo_data = geo_res.json()

        print("🧭 Geo IP Location:")
        print(f"  - Country: {geo_data.get('country')}")
        print(f"  - City: {geo_data.get('city')}")
        print(f"  - ISP: {geo_data.get('isp')}")
        print(f"  - Region: {geo_data.get('regionName')}")
        print(f"  - Org: {geo_data.get('org')}")
    except Exception as e:
        print("⚠️ Geolocation failed:", e)

    # Step 4: Crawl Links (First 10)
    try:
        print("\n🕷️ Internal Links Found (Top 10):")
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True) if domain in a['href'] or a['href'].startswith("/")]
        for i, link in enumerate(links[:10], 1):
            print(f"  [{i}] {link}")
    except Exception as e:
        print("⚠️ Crawling failed:", e)

    # Step 5: Check Headers
    try:
        print("\n📦 HTTP Headers:")
        head = requests.get(url, timeout=5)
        for k, v in head.headers.items():
            print(f"  {k}: {v}")
    except Exception as e:
        print("⚠️ Header check failed:", e)

    print("\n✅ Recon-X completed.\n")

