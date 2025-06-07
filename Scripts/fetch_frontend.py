import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .utils import save_results

def fetch_frontend_code(target):
    """
    Fetch html and js files from a target.
    """
    response = requests.get(f"http://{target}", timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    domain_dir = save_results(target, "html", response.text)

    # Save html
    with open(os.path.join(domain_dir, "html.txt"), "w", encoding="utf-8") as f:
        f.write(response.text)

    # Gather js
    js_list = []
    for script in soup.find_all("script"):
        if not script.get("src"):
            js_list.append(script.get_text())
    for script in soup.find_all("script", src=True):
        src = script.get("src")
        full_url = urljoin(target, src)
        try:
            js_resp = requests.get(full_url, timeout=5)
            js_list.append(js_resp.text)
        except:
            continue
    save_results(target, "js", "\n\n".join(js_list))

    return domain_dir
