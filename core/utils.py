import time
import sys
import re
from urllib.parse import urlparse

def print_slow(text, delay=0.03):
    """Print text character by character like a typewriter."""
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def is_ip(address):
    """Check if the input is a valid IP address."""
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", address) is not None

def clean_url_advanced(url, keep_port=False):
    """
    Normalize and clean URLs for scanning:
    - Adds http:// if missing
    - Keeps or removes custom ports
    - Removes path, query, fragment
    - Detects IPs and domains
    """
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    if not parsed.netloc:
        return ""

    hostname = parsed.hostname
    port = f":{parsed.port}" if parsed.port and keep_port else ""

    scheme = parsed.scheme
    cleaned = f"{scheme}://{hostname}{port}".rstrip("/")
    return cleaned

def clean_url(url):
    """Basic cleaner: adds http:// if missing, removes trailing slashes."""
    if not url.startswith("http"):
        url = "http://" + url
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}/"
    return base

# ✅ Advanced cleaner for new tools
def clean_url_advanced(url):
    """Advanced cleaner: removes scheme (http/https), www, and trailing slashes."""
    parsed = urlparse(url if url.startswith("http") else "http://" + url)
    domain = parsed.netloc.replace("www.", "").strip("/")
    return domain
