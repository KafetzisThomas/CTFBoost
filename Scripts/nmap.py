import re
import subprocess
from .utils import save_results

def quicknmap(target: str) -> tuple[str, str]:
    """
    Perform a quick nmap scan on the target.

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
    domain_dir = save_results(target, "quicknmap", output)
    return domain_dir, output

def fullnmap(target: str) -> tuple[str, str]:
    """
    Perform a full nmap scan on the target.

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
    domain_dir = save_results(target, "fullnmap", output)
    return domain_dir, output

def detect_web_service(nmap_output: str) -> bool:
    """
    Detect if a web service (HTTP/HTTPS) is running based on nmap output.
    """
    web_ports = re.findall(r"(\d+)/tcp\s+open\s+(http|https?)", nmap_output)
    return bool(web_ports)
