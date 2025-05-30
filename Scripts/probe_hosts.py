#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from .utils import save_results


def probe_host(target):
    output = []
    url = f"http://{target}"

    try:
        response = requests.get(url, timeout=5)
        line = f"{target} - {response.status_code}: {response.reason}"
        print(line)
        output.append(line)
    except requests.RequestException:
        line = f"{target} - Unreachable"
        print(line)
        output.append(line)

    save_results(target, "probehost", "\n".join(output))
