#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import subprocess
from colorama import Fore as F
from .utils import save_results


def check_ffuf():
    try:
        subprocess.run(["ffuf", "--version"], capture_output=True, text=True)
        print(f"{F.LIGHTBLUE_EX}OK: ffuf is installed.")
    except FileNotFoundError:
        print(f"{F.LIGHTBLUE_EX}* ffuf not found. Installing...")
        install_ffuf = subprocess.run(
            "sudo apt update && sudo apt install ffuf unzip -y",
            shell=True,
            capture_output=True,
            text=True,
        )
        print(install_ffuf.stdout)
        print(f"{F.LIGHTBLUE_EX}* ffuf installed successfully!")

    # Download and extract seclists
    if not os.path.isdir("SecLists-master"):
        print(f"{F.LIGHTBLUE_EX}* Downloading seclists...")
        subprocess.run(
            "wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip && unzip SecList.zip && rm -f SecList.zip",
            shell=True,
            capture_output=True,
            text=True,
        )


def directory_fuzzing(target):
    cmd = f"ffuf -u http://{target}/FUZZ -w SecLists-master/Discovery/Web-Content/common.txt"
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(output.stdout.rstrip())
    save_results(target, "ffufdir", output.stdout)


def subdomain_fuzzing(target):
    cmd = f"ffuf -u http://{target} -w SecLists-master/Discovery/DNS/bitquark-subdomains-top100000.txt -H 'Host:FUZZ.{target}' -fs 178"
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(output.stdout.rstrip())
    save_results(target, "ffufsub", output.stdout)
