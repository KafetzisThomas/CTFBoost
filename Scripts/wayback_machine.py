import json
import requests
from .utils import save_results

def wayback_machine(target: str) -> str:
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

    result_data = {"target": target, "total": len(snapshots), "snapshots": snapshots}
    output = json.dumps(result_data, indent=2) if snapshots else f"No Wayback Machine results found for {target}"
    domain_dir = save_results(target, "wayback", output)
    return domain_dir
