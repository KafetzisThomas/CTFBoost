#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess
from colorama import Fore as F


def check_nmap():
    result = subprocess.run(["nmap", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{F.LIGHTBLUE_EX}OK: Nmap is installed.")
    else:
        print(f"{F.LIGHTBLUE_EX}* Installing Nmap...")
        install_nmap = subprocess.run(
            "sudo apt update && sudo apt install nmap -y",
            shell=True,
            capture_output=True,
            text=True,
        )
        print(install_nmap.stdout)
        print(f"{F.LIGHTBLUE_EX}* Nmap installed successfully!")


def run_scan(target):
    print("---" * 28)
    run_nmap = subprocess.run(
        f"nmap {target}",
        shell=True,
        capture_output=True,
        text=True,
    )
    print(run_nmap.stdout.rstrip())
    print("---" * 28)
