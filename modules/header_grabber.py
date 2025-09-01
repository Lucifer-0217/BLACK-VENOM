import requests
from core.logger import log_result

def grab_headers(url):
    print(f"\n[🧪] Detecting WAF & grabbing headers for: {url}")
    try:
        response = requests.get(url, timeout=5)
        server = response.headers.get("Server", "Unknown")
        waf = "None Detected"

        # Basic WAF detection
        if "cloudflare" in server.lower():
            waf = "Cloudflare"
        elif "sucuri" in server.lower():
            waf = "Sucuri"
        elif "akamai" in server.lower():
            waf = "Akamai"
        elif "aws" in server.lower():
            waf = "AWS WAF"
        elif "f5" in server.lower():
            waf = "F5 BigIP"
        elif "imperva" in server.lower():
            waf = "Imperva Incapsula"

        print(f"\n  [🛰️] Server Header: {server}")
        print(f"  [🛡️] WAF Detection: {waf}")

        # Save to logs
        with open("logs/headers.txt", "a") as log:
            log.write(f"URL: {url}\nServer: {server}\nWAF: {waf}\n\n")

    except requests.RequestException as e:
        print(f"[❌] Error grabbing headers: {e}")

def detect_waf(response):
    headers = response.headers

    waf_signatures = {
        "cloudflare": ["cf-ray", "cf-cache-status"],
        "sucuri": ["x-sucuri-id", "x-sucuri-cache"],
        "aws": ["x-amzn-requestid", "x-amz-id-2"],
        "imperva": ["x-cdn", "x-iinfo"],
        "akamai": ["akamai-ghost", "x-akamai"],
    }

    detected = []
    for waf, sigs in waf_signatures.items():
        for sig in sigs:
            if any(sig.lower() in h.lower() for h in headers):
                detected.append(waf.capitalize())

    return ", ".join(detected) if detected else "None Detected"

def run(url):
    grab_headers(url)

