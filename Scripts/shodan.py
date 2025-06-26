import os
import json
from shodan import Shodan, APIError
from .utils import save_results

api = Shodan(os.getenv("SHODAN_API_KEY"))

def shodan_scan(target: str) -> str:
    """
    Perform shodan scan on the target.
    """
    try:
        ipinfo = api.host(target)
        data = json.dumps(ipinfo, indent=2)
    except APIError:
        data = f"No Shodan scan results found for {target}"

    header = f"=== Shodan scan results for {target} ===\n\n"
    output = header + data
    domain_dir = save_results(target, "shodan", output)
    return domain_dir
