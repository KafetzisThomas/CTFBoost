#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Script to install necessary tools and dependencies.

import shutil
import subprocess


def run_command(cmd: str) -> str:
    """
    Run shell command & return its output.
    """
    try:
        print(f"Running command: {cmd}")
        output = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        print(f"Command output: {output.stdout.strip()}")
        return output.stdout
    except subprocess.CalledProcessError as e:
        print(f"Failed to run command: {cmd}")
        print(f"Error: {e.output}")


def detect_package_manager() -> str:
    """
    Detect package manager based on the operating system.
    """
    managers = ["apt", "dnf", "yum", "pacman", "zypper", "brew", "apk"]
    for manager in managers:
        if shutil.which(manager):
            return manager
    return "unknown"


def update_upgrade_system(package_manager: str):
    """
    Update & upgrade the system.
    """
    print("Updating & upgrading the system...")
    if package_manager == "apt":
        run_command("sudo apt update && sudo apt upgrade -y")
    elif package_manager in ["dnf", "yum"]:
        run_command(f"sudo {package_manager} update -y")
    elif package_manager == "pacman":
        run_command("sudo pacman -Syu --noconfirm")
    elif package_manager == "zypper":
        run_command("sudo zypper update -y")
    elif package_manager == "apk":
        run_command("sudo apk update && sudo apk upgrade")
    print("System updated and upgraded successfully.")


def ensure_pip_installed(package_manager: str):
    """
    Ensure pip is installed.
    """
    if not shutil.which("pip3") and not shutil.which("pip"):
        print("pip is not installed. Installing pip...")
        if package_manager == "apt":
            run_command("sudo apt install python3-pip -y")
        elif package_manager in ["dnf", "yum"]:
            run_command(f"sudo {package_manager} install python3-pip -y")
        elif package_manager == "pacman":
            run_command("sudo pacman -S python-pip --noconfirm")
        elif package_manager == "zypper":
            run_command("sudo zypper install python3-pip -y")
        elif package_manager == "apk":
            run_command("sudo apk add py3-pip")
        elif package_manager == "brew":
            run_command("brew install python3")
        print("pip installed successfully.")
    else:
        print("pip is already installed.")


def install_tools(package_list: list[str]):
    """
    Install a package using the detected package manager.
    """
    manager = detect_package_manager()
    if manager == "unknown":
        print("No supported package manager found.")
        return

    if manager in ["apt", "dnf", "yum", "apk"]:
        cmd = ["sudo", manager, "install", "-y"] + package_list
    elif manager == "pacman":
        cmd = ["sudo", "pacman", "-S", "--noconfirm"] + package_list
    elif manager == "zypper":
        cmd = ["sudo", "zypper", "install", "-y"] + package_list
    elif manager == "brew":
        cmd = ["brew", "install"] + package_list

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("Package installation failed.")

def install_ollama():
    """
    Install Ollama and pull llama4 model for AI summaries.
    """
    subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, capture_output=True, text=True)
    print("Currently pulling 'llama4' but you can modify the code to use other models from https://ollama.com/library")
    subprocess.run(f"ollama pull llama4", shell=True, capture_output=True, text=True)

def main():
    package_manager = detect_package_manager()
    print("Detected package manager:", package_manager)

    update_upgrade_system(package_manager)
    ensure_pip_installed(package_manager)
    install_tools(["nmap", "ffuf", "unzip"])

    # Download and extract SecLists
    print("Downloading SecLists...")
    subprocess.run(
        "wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip && unzip SecList.zip && rm -f SecList.zip",
        shell=True,
        capture_output=True,
        text=True,
    )

    # Check if Ollama is installed, prompt user to install if not
    if shutil.which("ollama") is None:
        user_input = input("Ollama is not installed. Do you want to install it to enable AI summary reports? (Y/n): ")
        if user_input.strip().upper() == "Y":
                install_ollama()
    else:
        print("Ollama is already installed. Skipping installation.")

if __name__ == "__main__":
    main()
