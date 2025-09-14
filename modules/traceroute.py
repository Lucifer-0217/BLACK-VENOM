import platform
import subprocess
import re
import socket

def clean_target(target):
    # Remove http:// or https://
    target = re.sub(r'^https?://', '', target)
    return target.strip('/')

def run_traceroute(target):
    print("\n──────────────────────────────────────────────────────── 🛰️ Traceroute - Network Path Tracing ─────────────────────────────────────────────────────────")

    target = clean_target(target)

    try:
        # Resolve domain to IP
        ip = socket.gethostbyname(target)
        print(f"[📡] Target IP resolved: {ip}\n")
    except socket.gaierror:
        print(f"[⚠️] Unable to resolve target system name: {target}")
        print("\n────────────────────────────────────────────────────────────── 🌐 Traceroute Finished ───────────────────────────────────────────────────────────────")
        return

    system_platform = platform.system()

    try:
        if system_platform == "Windows":
            command = ["tracert", ip]
        else:
            command = ["traceroute", ip]

        # Run with timeout and capture output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        print(result.stdout)

    except subprocess.TimeoutExpired:
        print("[⏱️] Traceroute timed out. Target may be unreachable.")
    except Exception as e:
        print(f"[❌] Error running traceroute: {e}")

    print("\n────────────────────────────────────────────────────────────── 🌐 Traceroute Finished ───────────────────────────────────────────────────────────────")
