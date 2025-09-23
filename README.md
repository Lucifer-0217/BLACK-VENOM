# BLACK-VENOM

**BLACK-VENOM** is a modular cybersecurity toolkit for web reconnaissance, attack-surface enumeration, and initial vulnerability assessment. Implemented in Python 3, BLACK-VENOM aggregates common reconnaissance and scanning utilities into a single, terminal-driven interface to help security professionals collect, analyze, and retain findings in an auditable format.

---

> ⚠️ **Legal & Ethical Notice:** Use BLACK-VENOM **only** on systems and networks you own or where you have explicit written authorization to test. Unauthorized scanning, probing, or exploitation is unlawful and unethical.

> Lucifer-0217 and the BLACK-VENOM maintainers are not responsible for any unauthorized use of this toolkit.

---

## 🕷️ Features

* **Interactive Menu:** Terminal-based launcher with selectable modules.
* **Port Scanning:** Nmap-based scans to identify open ports and services.
* **WHOIS Lookup:** Domain registration and ownership details.
* **Subdomain Discovery:** Wordlist-driven subdomain enumeration.
* **HTTP Header Analysis:** Collect and inspect HTTP response headers.
* **Recon Modes:** Curated reconnaissance modes (e.g., CURSED, Recon‑X).
* **Robots.txt & Sitemap Fetching:** Automatic retrieval and parsing.
* **Traceroute & IP Geolocation:** Network path mapping and location lookup.
* **Exploit & Vulnerability Scanning:** Non-invasive detection checks and tech‑stack fingerprinting.
* **Reverse Shell Tools:** Payload generator/decoder strictly for lab use.
* **Comprehensive Logging:** All module outputs are persisted to the `logs/` directory.

---

## 🗂️ Directory Structure

* `core/` – Core utilities, configuration, banners, and wordlists
* `modules/` – Scanning, recon, OSINT, and analysis modules
* `logs/` – Saved scan outputs and logs
* `venom.py` – Main launcher script
* `requirements.txt` – Python dependencies

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.9+**
* Supported OS: Linux, macOS, Windows

### Installation

1. Verify Python:

```bash
python3 --version
```

2. Clone the repository:

```bash
git clone https://github.com/Lucifer-0217/BLACK-VENOM.git
cd BLACK-VENOM
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# or, if your environment requires it:
# pip3 install -r requirements.txt
```

4. Create the logs directory and phase subdirectories:

```bash
cd BLACK-VENOM

mkdir logs

cd logs

mkdir phase3 phase4 phase5

cd ..
```

---

## ⚡ Usage

Launch the tool:

```bash
python3 venom.py
```

When the interactive menu appears, choose a module by number and follow the prompts. Results from each run are written to the `logs/` directory.

> Use `python` in place of `python3` only if your system’s default `python` command targets Python 3.

---

## 🤝 Contributing

Contributions are welcome. Fork the repository, create a feature branch, and submit a pull request with a clear description of your changes.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

**Author:**

> **Disclaimer:** The author of BLACK-VENOM "Lucifer-0217" and "BLACK-VENOM" tool is not responsible for any unauthorized or illegal use of this toolkit. [Lucifer-0217](https://github.com/Lucifer-0217)
