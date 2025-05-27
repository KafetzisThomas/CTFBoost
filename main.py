#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: CTFBoost (https://github.com/KafetzisThomas/CTFBoost)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import subprocess
import colorama
from colorama import Fore as F

# Initialize colorama for colored output
colorama.init(autoreset=True)

print(
    rf"""{F.LIGHTGREEN_EX}
________________________________                   _____ 
__  ____/__  __/__  ____/__  __ )____________________  /_
_  /    __  /  __  /_   __  __  |  __ \  __ \_  ___/  __/
/ /___  _  /   _  __/   _  /_/ // /_/ / /_/ /(__  )/ /_  
\____/  /_/    /_/      /_____/ \____/\____//____/ \__/  


"""
)

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
    print(f"{F.LIGHTBLUE_EX}* Nmap installed sucessfully!")

ip = input("IP: ")
print("---" * 28)
run_nmap = subprocess.run(
    f"nmap {ip}",
    shell=True,
    capture_output=True,
    text=True,
)
print(run_nmap.stdout.rstrip())
print("---" * 28)
