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


def quicknmap(target):
    print(
        subprocess.run(
            f"nmap -T4 -F {target}",
            shell=True,
            capture_output=True,
            text=True,
        ).stdout.rstrip()
    )


def fullnmap(target):
    print(
        subprocess.run(
            f"nmap -p- -A -T4 -sVC -Pn {target}",
            shell=True,
            capture_output=True,
            text=True,
        ).stdout.rstrip()
    )
