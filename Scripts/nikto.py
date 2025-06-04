import subprocess
from .utils import save_results

def nikto(target: str) -> tuple[str, str]:
    cmd = f"nikto -h {target}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output = ""
    for line in process.stdout:
        print(line, end='')
        output += line
    process.wait()
    domain_dir = save_results(target, "nikto", output)
    return domain_dir, output
