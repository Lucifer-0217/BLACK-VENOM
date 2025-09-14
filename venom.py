from core.banner import show_banner
from core.config import load_config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Phase 1 & 2 Tools
from modules import (
    scan_port,
    whois_lookup,
    subdomain_finder,
    header_grabber,
    cursed_recon,
    robots_sitemap,
    traceroute,
    ip_location,
    osint_scan
)

# Phase 3 Tools
from modules.phase3 import (
    exploit_scanner,
    xmode_crawler,
    shell_detector,
    tech_fingerprint
)

# Phase 3 UPGRADE
from modules.phase3_upgrade import recon_x

# Phase 4 — Hardcore Exploit Recon
from modules.phase4 import (
    nuclei_scan,
    find_exploits,
    parse_vulns,
    aira_suggest,
)

# ✅ Phase 5 — Reverse Shell Tools
from modules.phase5.reverse_shell_gen import generate_reverse_shell
from modules.phase5.reverse_shell_decoder import decode_chain


def main():
    show_banner()
    config = load_config()

    print("\n🛠️  TOOLS MENU")
    print("[1]  🔍 Port Scanner")
    print("[2]  🌐 WHOIS Lookup")
    print("[3]  🧭 Subdomain Finder")
    print("[4]  🧾 Header Grabber")
    print("[5]  🧨 CURSED Recon Mode")
    print("[6]  🤖 Robots.txt + Sitemap")
    print("[7]  🛰️ Traceroute")
    print("[8]  💥 Exploit Scanner")
    print("[9]  🕷️ XMode Crawler")
    print("[10] 🐚 Web Shell Detector")
    print("[11] 🧬 Tech Stack Fingerprint")
    print("[12] 🧭 IP Geolocation")
    print("[13] 🧠 OSINT Scanner")
    print("[14] 🧪 Recon-X (Upgraded)")
    print("[15] ⚔️ Exploit AutoScan (Nuclei + CVE + AIRA)")
    print("[16] 💣 Reverse Shell Payload Generator")
    print("[17] 🔓 Decode Obfuscated Reverse Shell Payload")

    choice = input("\nSelect an option (1–17): ")

    if choice == "1":
        target = input("Enter target IP/Host: ")
        scan_port.run(target)

    elif choice == "2":
        domain = input("Enter domain: ")
        whois_lookup.run(domain)

    elif choice == "3":
        domain = input("Enter domain (without http/https): ")
        subdomain_finder.run(domain)

    elif choice == "4":
        url = input("Enter full URL (e.g. https://example.com): ")
        header_grabber.run(url)

    elif choice == "5":
        target = input("Enter target domain or IP: ")
        cursed_recon.run(target)

    elif choice == "6":
        domain = input("Enter domain (without http/https): ")
        robots_sitemap.run(domain)

    elif choice == "7":
        domain = input("Enter domain or IP: ")
        traceroute.run_traceroute(domain)

    elif choice == "8":
        domain = input("Enter domain or IP: ")
        exploit_scanner.run(domain)

    elif choice == "9":
        domain = input("Enter domain or IP: ")
        xmode_crawler.run(domain)

    elif choice == "10":
        domain = input("Enter domain or IP: ")
        shell_detector.run(domain)

    elif choice == "11":
        domain = input("Enter domain or IP: ")
        tech_fingerprint.run(domain)

    elif choice == "12":
        ip = input("Enter IP address or domain: ")
        ip_location.run(ip)

    elif choice == "13":
        domain = input("Enter domain or username (for OSINT): ")
        osint_scan.run(domain)

    elif choice == "14":
        recon_x.recon_x()

    elif choice == "15":
        target = input("Enter target domain or IP: ")
        nuclei_scan(target)

        print("\n[📁] After scan completes, go to logs/phase4/ and choose the latest output file.")
        log_file = input("Enter path to the scan log file: ")
        cves = parse_vulns(log_file)

        print("\n[🤖 AIRA SUGGESTS]:")
        aira_suggest(cves)

        keyword = input("Enter keyword for exploit search (or leave blank): ")
        if keyword:
            find_exploits(keyword)

    elif choice == "16":
        ip = input("Enter IP: ")
        port = input("Enter Port: ")
        lang = input("Choose language (bash/python/php/powershell/perl/node): ").lower()
        obfuscate = input("Obfuscate payload? (y/n): ").lower() == 'y'
        generate_reverse_shell(ip, port, lang, obfuscate)

    elif choice == "17":
        payload = input("Enter obfuscated payload: ")
        key = input("Enter XOR key (leave blank if none): ")
        decode_chain(payload, key if key else None)

    else:
        print("❌ Invalid choice. Please select between 1 to 17.")


if __name__ == "__main__":
    main()
