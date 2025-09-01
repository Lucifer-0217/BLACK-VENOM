from colorama import Fore, Style

def show_banner():
    banner = f"""
{Fore.LIGHTGREEN_EX}
██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║
██████╔╝██║     ███████║██║     █████╔╝     ██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗     ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝
{Style.BRIGHT + Fore.RED}                           BLACK VENOM — Hacker's Recon Arsenal™{Style.RESET_ALL}
    """
    print(banner)
    print(Fore.MAGENTA + "\n💀 Let the venom spread across the net... silently, fatally.\n" + Style.RESET_ALL)
