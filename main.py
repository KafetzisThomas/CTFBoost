#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: CTFBoost (https://github.com/KafetzisThomas/CTFBoost)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import sys
import argparse
import colorama
from colorama import Fore as F
from Scripts.probe_hosts import probe_host
from Scripts.nmap import quicknmap, fullnmap, detect_web_service
from Scripts.ffuf import directory_fuzzing, subdomain_fuzzing
from Scripts.dns_enum import dns_enumeration
from Scripts.utils import generate_report

# Initialize colorama for colored output
colorama.init(autoreset=True)


banner = rf"""{F.LIGHTGREEN_EX}
________________________________                   _____ 
__  ____/__  __/__  ____/__  __ )____________________  /_
_  /    __  /  __  /_   __  __  |  __ \  __ \_  ___/  __/
/ /___  _  /   _  __/   _  /_/ // /_/ / /_/ /(__  )/ /_  
\____/  /_/    /_/      /_____/ \____/\____//____/ \__/  

By KafetzisThomas
"""


def main():
    print(banner)
    print("---" * 28)

    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="target host or ip address")
    parser.add_argument("--probe", action="store_true", help="probe the host")
    parser.add_argument(
        "--dnsenum", action="store_true", help="perform dns enumeration"
    )
    parser.add_argument(
        "--quicknmap", action="store_true", help="run a quick nmap scan"
    )
    parser.add_argument("--fullnmap", action="store_true", help="run a full nmap scan")
    parser.add_argument(
        "--ffufdir", action="store_true", help="perform directory fuzzing with ffuf"
    )
    parser.add_argument(
        "--ffufsub", action="store_true", help="perform subdomain fuzzing with ffuf"
    )
    parser.add_argument(
        "--ai-report", action="store_true", help="generate ai summary report of all scan results"
    )

    args = parser.parse_args()
    target = args.target
    domain_dir = None
    output = ""

    # Host probing
    if args.probe:
        domain_dir = probe_host(target)

    # DNS enumeration
    if args.dnsenum:
        domain_dir = dns_enumeration(target)

    # Nmap
    if args.quicknmap:
        domain_dir, output = quicknmap(target)
    elif args.fullnmap:
        domain_dir, output = fullnmap(target)

    # ffuf
    if detect_web_service(output):
        if args.ffufdir:
            domain_dir = directory_fuzzing(target)
        elif args.ffufsub:
            domain_dir = subdomain_fuzzing(target)

    if args.ai_report:
        generate_report(domain_dir)

    print("---" * 28)

if __name__ == "__main__":
    main()
