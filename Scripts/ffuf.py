#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess
from .utils import save_results


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
