<h1 align="center">CTFBoost</h1>

**What is this?**  
A recon tool for bug bounty hunters that simplifies and automates the enumeration process during security assessments.

## Features

* HTTP host probing
* DNS record scanning
* IP address extraction
* Port scanning
* Web server detection
* Service/version detection
* Shodan integration for additional recon
* Dir/subdir fuzzing
* Web vulnerability scanning with Nikto
* Fetch html and js files
* Results saved per IP/domain
* AI generated summary report with OpenAI/Ollama models

## Installation

```bash
git clone https://github.com/KafetzisThomas/CTFBoost.git
cd CTFBoost
pip3 install -r requirements.txt
mv .env.example .env
nano .env  # modify file, instructions inside
sudo python3 install.py
```

## Usage

```bash
usage: main.py [-h] [--probe] [--shodan] [--dnsenum] [--quicknmap] [--fullnmap] [--ffufdir] [--ffufsub] [--nikto] [--frontend-fetch] [--ai-report] target

positional arguments:
  target            target host or ip address

options:
  -h, --help        show this help message and exit
  --probe           probe the host
  --shodan          fetch shodan info
  --dnsenum         perform dns enumeration
  --quicknmap       run a quick nmap scan
  --fullnmap        run a full nmap scan
  --ffufdir         perform directory fuzzing with ffuf
  --ffufsub         perform subdomain fuzzing with ffuf
  --nikto           scan for web vulnerabilities using nikto
  --frontend-fetch  fetch front end files (html,css,js)
  --ai-report       generate ai summary report of all scan results
```

## Examples

Probe the target:
```bash
python3 main.py <ip/domain> --probe
```

Search target with shodan:
```bash
python3 main.py <ip/domain> --shodan
```

DNS record scan:
```bash
python3 main.py <ip/domain> --dnsenum
```

Quick nmap scan:
```bash
python3 main.py <ip/domain> --quicknmap
```

Full nmap scan:
```bash
python3 main.py <ip/domain> --fullnmap
```

Fuzz for directories with ffuf:
```bash
python3 main.py <ip/domain> --quicknmap --ffufdir
```

Fuzz for subdomains with ffuf:
```bash
python3 main.py <ip/domain> --quicknmap --ffufsub
```

Web vulnerability scanning with nikto:
```bash
python3 main.py <ip/domain> --quicknmap --nikto
```

Fetch html and js files:
```bash
python3 main.py <ip/domain> --quicknmap --frontend-fetch
```

Generate an AI summary report:
```bash
python3 main.py <ip/domain> --probe --quicknmap --ai-report
```

**Note:** Flags can be combined to run multiple scans in one command.

## Disclaimer: Educational Use Only

**CTFBoost** is a tool for `learning` and `practicing` recon techniques in ethical hacking, bug bounty hunting and CTFs. It must only be used on systems you own or have permission to test.

**The author and contributors are NOT responsible for misuse, damage or legal consequences resulting from this tool.**

Use responsibly and for **educational purposes only**.
