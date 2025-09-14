# modules/phase5/reverse_shell_decoder.py

import base64
import zlib
import re

def xor_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def clean_base64_input(raw: str) -> str:
    """
    Extract only the base64 string from full payloads like:
    echo <base64> | base64 -d | bash
    """
    match = re.search(r'echo\s+([A-Za-z0-9+/=]+)', raw)
    if match:
        return match.group(1)
    return raw.strip()

def decode_chain(payload: str, key: str = None):
    try:
        # Step 0: Extract clean base64 string if user pasted full shell
        payload = clean_base64_input(payload)

        # Step 1: Base64 decode
        decoded = base64.b64decode(payload)
        print("[🔓] Base64 decoded ✔️")

        # Step 2: Optional XOR decrypt
        if key:
            decoded = xor_decrypt(decoded, key.encode())
            print("[🔓] XOR decrypted ✔️")

        # Step 3: Optional zlib decompress
        try:
            decoded = zlib.decompress(decoded)
            print("[🌀] zlib decompressed ✔️")
        except zlib.error:
            print("[⚠️] Not zlib-compressed or already decompressed.")

        print("\n[✅] Final Decoded Payload:")
        print("=" * 50)
        print(decoded.decode(errors='replace'))
        print("=" * 50)
    except Exception as e:
        print(f"[❌] Decode failed: {e}")
