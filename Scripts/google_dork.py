import os
from serpapi import GoogleSearch
from .utils import save_results

GoogleSearch.SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

DORKS = [
    'site:{target} ext:sql',
    'site:{target} ext:bak',
    'site:{target} intitle:"index of"',
    'site:{target} inurl:admin',
    'site:{target} ext:env',
    'site:{target} filetype:log',
    'site:{target} ext:json inurl:api',
    'site:{target} ext:js'
]

def google_dork(target: str) -> str:
    results = []
    for dork in DORKS:
        query = dork.format(target=target)
        search = GoogleSearch({"q": query, "num": 10})
        data = search.get_dict()

        for result in data.get("organic_results", []):
            title = result.get("title")
            link = result.get("link")
            results.append(f"{query} | {title} | {link}") if link else None

    output = "\n".join(results) if results else f"No Google dork results found for {target}"
    domain_dir = save_results(target, "google", output)
    return domain_dir
