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

def analyze_security_headers(response_headers: dict) -> dict[str, list[str]]:
    """
    Analyze HTTP response headers for presence of key security headers.
    """
    security_headers = {
        'content-security-policy': 'CSP',
        'x-frame-options': 'Clickjacking Protection',
        'x-content-type-options': 'MIME Sniffing Protection',
        'strict-transport-security': 'HSTS',
        'x-xss-protection': 'XSS Protection'
    }

    headers_lower = {}
    for key, value in response_headers.items():
        headers_lower[key.lower()] = value

    present = []
    missing = []
    for header, description in security_headers.items():
        if header in headers_lower:
            present.append(f"{description}: {headers_lower[header]}")
        else:
            missing.append(description)

    return {'missing': missing, 'present': present}

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

        # Analyze security headers on successful responses
        if response.status_code == 200:
            header_analysis = analyze_security_headers(response.headers)
            results.append(f"\n=== Security Headers Analysis for {target} ===\n")
            if header_analysis['missing']:
                results.append("Missing:")
                for header in header_analysis['missing']:
                    results.append(f"\t- {header}")
            if header_analysis['present']:
                results.append("Present:")
                for header in header_analysis['present']:
                    results.append(f"\t- {header}")

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
