#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: CTFBoost (https://github.com/KafetzisThomas/CTFBoost)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import sys
import colorama
from colorama import Fore as F
from Scripts.probe_hosts import probe_host
from Scripts.nmap import check_nmap, quicknmap, fullnmap, detect_web_service
from Scripts.ffuf import check_ffuf, directory_fuzzing, subdomain_fuzzing
from Scripts.dns_enum import dns_enumeration

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
    output = ""

    # Host probing
    if "probe" in sys.argv:
        probe_host(sys.argv[1])

    # DNS enumeration
    if "dnsenum" in sys.argv:
        dns_enumeration(sys.argv[1])

    # Nmap
    if "quicknmap" in sys.argv:
        check_nmap()
        output = quicknmap(target=sys.argv[1])
    elif "fullnmap" in sys.argv:
        check_nmap()
        output = fullnmap(target=sys.argv[1])

    # fuff
    if detect_web_service(output):
        if "ffufdir" in sys.argv:
            check_ffuf()
            directory_fuzzing(target=sys.argv[1])
        elif "ffufsub" in sys.argv:
            check_ffuf()
            subdomain_fuzzing(target=sys.argv[1])

    print("---" * 28)


if __name__ == "__main__":
    main()
