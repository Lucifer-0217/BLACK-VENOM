# modules/robots_sitemap.py

import requests
from rich.console import Console
from urllib.parse import urljoin

console = Console()

def fetch_robots(domain):
    robots_url = urljoin(f"http://{domain}", "/robots.txt")
    console.print(f"\n[bold cyan]🔎 Fetching robots.txt from: {robots_url}")
    try:
        response = requests.get(robots_url, timeout=5)
        if response.status_code == 200:
            console.print("[green]✓ robots.txt found:\n")
            print(response.text)
        else:
            console.print("[red]✘ robots.txt not found or inaccessible.")
    except Exception as e:
        console.print(f"[red]✘ Error: {e}")

def fetch_sitemap(domain):
    sitemap_url = urljoin(f"http://{domain}", "/sitemap.xml")
    console.print(f"\n[bold cyan]🧭 Fetching sitemap.xml from: {sitemap_url}")
    try:
        response = requests.get(sitemap_url, timeout=5)
        if response.status_code == 200:
            console.print("[green]✓ sitemap.xml found:\n")
            print(response.text[:1500])  # Limit output to 1500 chars
        else:
            console.print("[red]✘ sitemap.xml not found or inaccessible.")
    except Exception as e:
        console.print(f"[red]✘ Error: {e}")

def run(domain):
    console.rule("[bold magenta]🤖 ROBOTS & SITEMAP EXTRACTOR")
    fetch_robots(domain)
    fetch_sitemap(domain)
    console.rule("[bold magenta]🗂️ Extraction Complete")
