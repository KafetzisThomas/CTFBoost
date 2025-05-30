#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import subprocess
from colorama import Fore as F
from .utils import save_results


def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], capture_output=True, text=True)
        print(f"{F.LIGHTBLUE_EX}OK: Nmap is installed.")
    except FileNotFoundError:
        print(f"{F.LIGHTBLUE_EX}* Nmap not found. Installing...")
        install_nmap = subprocess.run(
            "sudo apt update && sudo apt install nmap -y",
            shell=True,
            capture_output=True,
            text=True,
        )
        print(install_nmap.stdout)
        print(f"{F.LIGHTBLUE_EX}* Nmap installed successfully!")


def quicknmap(target):
    result = subprocess.run(
        f"nmap -T4 -F {target}",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout
    output = result
    print(output.rstrip())
    save_results(target, "quicknmap", output)
    return output


def fullnmap(target):
    result = subprocess.run(
        f"nmap -p- -A -T4 -sVC -Pn {target}",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout
    output = result
    print(output.rstrip())
    save_results(target, "fullnmap", output)
    return output


def detect_web_service(nmap_output):
    # Simple regex to find open ports 80 or 443 (http/https)
    web_ports = re.findall(r"(\d+)/tcp\s+open\s+(http|https?)", nmap_output)
    return bool(web_ports)
