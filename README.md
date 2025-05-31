<h1 align="center">CTFBoost</h1>

**What is this?**  
A recon tool for bug bounty hunters that simplifies and automates the enumeration process during security assessments.

## Features

* HTTP host probing
* DNS record scanning
* Port scanning
* Dir/subdir fuzzing
* Results saved per IP/domain

## Installation

```bash
git clone https://github.com/KafetzisThomas/CTFBoost.git
cd CTFBoost
pip3 install -r requirements.txt
sudo python3 install.py
```

## Usage

```bash
usage: main.py [-h] [--probe] [--dnsenum] [--quicknmap] [--fullnmap] [--ffufdir] [--ffufsub] target

positional arguments:
  target       target host or ip address

options:
  -h, --help   show this help message and exit
  --probe      probe the host
  --dnsenum    perform dns enumeration
  --quicknmap  run a quick nmap scan
  --fullnmap   run a full nmap scan
  --ffufdir    perform directory fuzzing with ffuf
  --ffufsub    perform subdomain fuzzing with ffuf
```

## Examples

Probe the target:
```bash
python3 main.py <ip/domain> --probe
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
python3 main.py <ip/domain> --ffufdir
```

Fuzz for subdomains with ffuf:
```bash
python3 main.py <ip/domain> --ffufsub
```

**Note:** Flags can be combined to run multiple scans in one command.

## Disclaimer: Educational Use Only

**CTFBoost** is a tool for `learning` and `practicing` recon techniques in ethical hacking, bug bounty hunting and CTFs. It must only be used on systems you own or have permission to test.

**The author and contributors are NOT responsible for misuse, damage or legal consequences resulting from this tool.**

Use responsibly and for **educational purposes only**.
