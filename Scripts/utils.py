import os
from datetime import datetime
from colorama import Fore as F


def save_results(target, scan_type, output):
    """
    Save scan results to a ip/domain specific directory.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    domain_dir = f"scans/{target}_{timestamp}"
    os.makedirs(domain_dir, exist_ok=True)
    file_path = f"{domain_dir}/{scan_type}.txt"
    with open(file_path, "w") as f:
        f.write(output)
    print(f"{F.LIGHTGREEN_EX}Results saved to: {file_path}")
