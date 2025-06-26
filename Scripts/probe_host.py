import requests
import socket
import ipaddress
from .utils import save_results

def is_ip(address: str) -> bool:
    """
    Check if the given string is an IP address or domain.
    """
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def probe_host(target: str) -> str:
    """
    Probe target by sending a GET request.
    """
    results = []
    url = f"http://{target}"

    try:
        response = requests.get(url, timeout=5)
        line = f"{target} - {response.status_code}: {response.reason}"
        print(line)
        results.append(line)

        # If target is domain resolve to IP and prompt user to add to /etc/hosts
        if not is_ip(target):
            ip = socket.gethostbyname(target)
            print(f"Add to /etc/hosts: {ip} {target}")
            input("Press Enter once done...")
    except requests.RequestException:
        line = f"{target} - Unreachable"
        print(line)
        results.append(line)

    output = f"=== HTTP host probing results for {target} ===\n\n"
    output += "\n".join(results)
    domain_dir = save_results(target, "probehost", output)
    return domain_dir
