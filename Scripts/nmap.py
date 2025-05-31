#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import subprocess
from .utils import save_results


def quicknmap(target: str) -> str:
    """
    -T4: set aggressive timing for faster execution.
    -F: fast mode, scans fewer common ports (~100).
    -v: add verbosity (doesn't affect speed).
    """
    cmd = f"nmap -T4 -F -v {target}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output = ""
    for line in process.stdout:
        print(line, end='')
        output += line
    process.wait()
    save_results(target, "quicknmap", output)
    return output


def fullnmap(target: str) -> str:
    """
    -p-: scan all 65,535 ports.
    -A: enable os detection, version detection, script scanning and traceroute.
    -T4: set aggressive timing for faster execution (still heavy though).
    -sVC: run version detection and default scripts.
    -Pn: skip host discovery (scan even if host seems down).
    -v: add verbosity (doesn't affect speed).
    """
    cmd = f"nmap -p- -A -T4 -sVC -Pn -v {target}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output = ""
    for line in process.stdout:
        print(line, end='')
        output += line
    process.wait()
    save_results(target, "fullnmap", output)
    return output


def detect_web_service(nmap_output: str) -> bool:
    # Simple regex to find open ports 80 or 443 (http/https)
    web_ports = re.findall(r"(\d+)/tcp\s+open\s+(http|https?)", nmap_output)
    return bool(web_ports)
