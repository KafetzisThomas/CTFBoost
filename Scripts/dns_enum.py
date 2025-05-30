import dns.resolver
from colorama import Fore as F
from .utils import save_results


def dns_enumeration(target):
    """
    Perform DNS enumeration for the given target.

    A: maps a hostname to an IPv4 address.
    AAAA: maps a hostname to an IPv6 address.
    MX: lists mail servers handling email for the target.
    NS: shows name servers responsible for the target's DNS.
    TXT: contains arbitrary text often for verification or policies.
    """
    records = ["A", "AAAA", "MX", "NS", "TXT"]
    output = []

    for record in records:
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ["1.1.1.1"]
            answers = resolver.resolve(target, record)
            for rdata in answers:
                line = f"{record}: {rdata.to_text()}"
                print(f"{F.LIGHTGREEN_EX}{line}")
                output.append(line)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"{F.LIGHTRED_EX}{record}: No record found")

    save_results(target, "dnsenum", "\n".join(output))
