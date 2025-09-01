# modules/scan_port.py

import socket
from core.utils import print_slow
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
    except Exception:
        pass

def run(target):
    print_slow(f"\n[+] Scanning active ports on {target}...\n")

    # Dynamically scan a wide active port range (common)
    active_port_range = list(range(1, 1025))  # Modify range here if needed

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in active_port_range:
            executor.submit(scan_port, target, port)

    print("\n[✔] Scan complete.")
