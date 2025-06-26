import json
import requests
from .utils import save_results

def wayback_machine(target: str) -> str:
    """
    Fetch archived snapshots of the target.
    """
    url = "http://web.archive.org/cdx/search/cdx"
    params = {
        "url": f"{target}/*",
        "output": "json",
        "fl": "timestamp,original",
        "collapse": "urlkey"
    }

    snapshots = []
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for timestamp, url in data[1:]:
            snapshots.append({
                "timestamp": timestamp,
                "original": url,
                "snapshot_url": f"https://web.archive.org/web/{timestamp}/{url}"
            })

    results = {"target": target, "total": len(snapshots), "snapshots": snapshots}
    output = f"=== Wayback Machine scan results for {target} ===\n\n"
    if snapshots:
        output += json.dumps(results, indent=2)
    else:
        output += f"No Wayback Machine scan results found for {target}"
    domain_dir = save_results(target, "wayback", output)
    return domain_dir
