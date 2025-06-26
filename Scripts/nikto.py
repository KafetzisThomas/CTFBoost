import subprocess
from .utils import save_results

def nikto(target: str) -> str:
    """
    Perform a web vulnerability scan on the target.

    -h: specify target/domain
    """
    cmd = f"nikto -h {target}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    header = f"=== Nikto vulnerability scan results for {target} ===\n\n"
    output = header
    for line in process.stdout:
        print(line, end='')
        output += line
    process.wait()
    domain_dir = save_results(target, "nikto", output)
    return domain_dir
