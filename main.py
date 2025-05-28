#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: CTFBoost (https://github.com/KafetzisThomas/CTFBoost)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import sys
import colorama
from colorama import Fore as F
from Scripts.nmap import check_nmap, quicknmap, fullnmap

# Initialize colorama for colored output
colorama.init(autoreset=True)


banner = rf"""{F.LIGHTGREEN_EX}
________________________________                   _____ 
__  ____/__  __/__  ____/__  __ )____________________  /_
_  /    __  /  __  /_   __  __  |  __ \  __ \_  ___/  __/
/ /___  _  /   _  __/   _  /_/ // /_/ / /_/ /(__  )/ /_  
\____/  /_/    /_/      /_____/ \____/\____//____/ \__/  


"""


def main():
    print(banner)
    print("---" * 28)
    if "quicknmap" in sys.argv:
        check_nmap()
        quicknmap(target=sys.argv[1])
    elif "fullnmap" in sys.argv:
        check_nmap()
        fullnmap(target=sys.argv[1])
    print("---" * 28)


if __name__ == "__main__":
    main()
