import subprocess
from .utils import save_results

def directory_fuzzing(target: str) -> str:
    """
    Perform directory fuzzing on the target.

    -u: url to fuzz
    -w: wordlist used
    """
    cmd = f"ffuf -u http://{target}/FUZZ -w SecLists-master/Discovery/Web-Content/common.txt"
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(output.stdout.rstrip())
    domain_dir = save_results(target, "ffufdir", output.stdout)
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
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(output.stdout.rstrip())
    domain_dir = save_results(target, "ffufsub", output.stdout)
    return domain_dir
