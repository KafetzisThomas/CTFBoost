#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Script to install necessary tools and dependencies.

import os
import shutil
import subprocess
from dotenv import load_dotenv

load_dotenv()

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


def ensure_uv_installed():
    """
    Ensure uv is installed.
    """
    if not shutil.which("uv"):
        print("uv is not installed. Installing uv...")
        run_command("curl -LsSf https://astral.sh/uv/install.sh | sh")
        print("uv installed successfully.")
    else:
        print("uv is already installed.")


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
        run_command(cmd)
    except subprocess.CalledProcessError:
        print("Package installation failed.")

def install_ollama(model_name: str):
    """
    Install Ollama and pull user selected model for AI summaries.
    Skip installation if using an OpenAI hosted model.
    """
    if model_name.startswith("gpt-"):
        print(f"{model_name} is OpenAI hosted. No need to install locally.")
        return

    # Check if Ollama is installed, prompt user to install if not
    if shutil.which("ollama") is None:
        user_input = input("Ollama is not installed. Install it to enable AI summary reports? (Y/n): ")
        if user_input.strip().lower() not in ("", "y", "yes"):
            return
        run_command("curl -fsSL https://ollama.com/install.sh | sh")

    print(f"Pulling '{model_name}' model from Ollama...")
    run_command(f"ollama pull {model_name}")

def main():
    package_manager = detect_package_manager()
    print("Detected package manager:", package_manager)

    update_upgrade_system(package_manager)
    ensure_uv_installed()
    install_tools(["nmap", "ffuf", "nikto", "unzip"])
    install_ollama(os.getenv("LLM_NAME"))

    # Download and extract SecLists
    print("Downloading SecLists...")
    run_command("wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip && unzip SecList.zip && rm -f SecList.zip")

if __name__ == "__main__":
    main()
