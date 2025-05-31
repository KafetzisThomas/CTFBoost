#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import socket
import ipaddress
from .utils import save_results

def is_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def probe_host(target):
    output = []
    url = f"http://{target}"

    try:
        response = requests.get(url, timeout=5)
        line = f"{target} - {response.status_code}: {response.reason}"
        print(line)
        output.append(line)

        # If target is domain resolve to IP and prompt user to add to /etc/hosts
        if not is_ip(target):
            ip = socket.gethostbyname(target)
            print(f"Add to /etc/hosts: {ip} {target}")
            input("Press Enter once done...")
    except requests.RequestException:
        line = f"{target} - Unreachable"
        print(line)
        output.append(line)

    save_results(target, "probehost", "\n".join(output))
