import os
import json
from shodan import Shodan
from .utils import save_results

api = Shodan(os.getenv("SHODAN_API_KEY"))

def shodan_scan(target: str) -> str:
    """
    Perform shodan scan on the target.
    """
    ipinfo = api.host('8.8.8.8')
    data = json.dumps(ipinfo, indent=2)
    domain_dir = save_results(target, "shodan", data)
    return domain_dir
