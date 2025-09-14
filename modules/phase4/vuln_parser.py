# modules/phase4/vuln_parser.py
import re

def parse_vulns(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    cves = []
    for line in lines:
        match = re.findall(r'CVE-\d{4}-\d{4,7}', line)
        if match:
            cves.extend(match)

    unique_cves = sorted(set(cves))
    print("[🧠] Unique CVEs found:")
    for cve in unique_cves:
        print(f" - {cve}")
    return unique_cves
