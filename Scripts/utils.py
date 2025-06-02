import os
import subprocess
from datetime import datetime
from colorama import Fore as F

def save_results(target: str, scan_type: str, output: str) -> str:
    """
    Save scan results to an ip/domain specific directory.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    domain_dir = f"scans/{target}_{timestamp}"
    os.makedirs(domain_dir, exist_ok=True)
    file_path = f"{domain_dir}/{scan_type}.txt"
    with open(file_path, "w") as f:
        f.write(output)
    print(f"{F.LIGHTGREEN_EX}Results saved to: {file_path}")
    return domain_dir

def generate_report(domain_dir: str) -> str:
    """
    Generate an AI summary report from all text files in the scan directory.
    """
    combined_text = ""
    for filename in os.listdir(domain_dir):
        if filename.endswith(".txt") and filename != "report.md":
            file_path = os.path.join(domain_dir, filename)
            with open(file_path, "r") as f:
                combined_text += f"\n\n--- {filename} ---\n" + f.read()

    prompt = f"Summarize the following scan results into a concise markdown report with findings and recommendations:\n{combined_text}"
    ai_summary = subprocess.run(['ollama', 'run', 'llama4'], input=prompt, capture_output=True, text=True).stdout

    report_path = os.path.join(domain_dir, "report.md")
    with open(report_path, "w") as report_file:
        report_file.write(f"## Recon Summary Report\n\n{ai_summary}")

    print(f"{F.LIGHTGREEN_EX}AI report saved to: {report_path}")
    return report_path
