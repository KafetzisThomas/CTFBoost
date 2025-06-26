import os
import json
from shodan import Shodan
from .utils import save_results

api = Shodan(os.getenv("SHODAN_API_KEY"))

def shodan_scan(target: str) -> str:
    """
    Perform shodan scan on the target.
    """
    ipinfo = api.host(target)
    data = json.dumps(ipinfo, indent=2)
    header = f"=== Shodan scan results for {target} ===\n\n"
    output = header + data
    domain_dir = save_results(target, "shodan", output)
    return domain_dir
