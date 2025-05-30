import dns.resolver
from colorama import Fore as F


def dns_enumeration(domain):
    """
    Perform DNS enumeration for the given domain.

    A: maps a domain to an IPv4 address.
    AAAA: maps a domain to an IPv6 address.
    MX: lists mail servers handling email for the domain.
    NS: shows name servers responsible for the domain's DNS.
    TXT: contains arbitrary text, often for verification or policies.
    """
    records = ["A", "AAAA", "MX", "NS", "TXT"]
    print(f"{F.LIGHTBLUE_EX}DNS Enumeration for: {domain}")
    for record in records:
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ["1.1.1.1"]
            answers = resolver.resolve(domain, record)
            for rdata in answers:
                print(f"{F.LIGHTGREEN_EX}{record}: {rdata.to_text()}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"{F.LIGHTRED_EX}{record}: No record found")
