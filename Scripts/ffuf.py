import subprocess
from .utils import save_results

def directory_fuzzing(target: str) -> str:
    """
    Perform directory fuzzing on the target.

    -u: url to fuzz
    -w: wordlist used
    """
    cmd = f"ffuf -u http://{target}/FUZZ -w SecLists-master/Discovery/Web-Content/common.txt"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output = ""
    for line in process.stdout:
        print(line, end='')
        output += line
    domain_dir = save_results(target, "ffufdir", output)
    return domain_dir

def subdomain_fuzzing(target: str) -> str:
    """
    Perform subdomain fuzzing on the target.

    -u: url to fuzz
    -w: wordlist used
    -H: specify host
    -fs: exclude irrelevant results
    """
    cmd = f"ffuf -u http://{target} -w SecLists-master/Discovery/DNS/bitquark-subdomains-top100000.txt -H 'Host:FUZZ.{target}' -fs 178"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output = ""
    for line in process.stdout:
        print(line, end='')
        output += line
    process.wait()
    domain_dir = save_results(target, "ffufsub", output)
    return domain_dir
