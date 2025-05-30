#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from colorama import Fore as F


def probe_host(target):
    print(f"{F.LIGHTBLUE_EX}Probing host:", target)
    url = f"http://{target}"
    try:
        response = requests.get(url, timeout=5)
        print(f"{target} - {response.status_code}: {response.reason}")
    except requests.RequestException:
        print(f"{target} - Unreachable")
