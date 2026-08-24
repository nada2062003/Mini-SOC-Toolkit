from urllib.parse import urlparse
import ipaddress
from datetime import datetime


def run_phishing_analyzer():

    print("\n" + "=" * 50)
    print("          PHISHING URL ANALYZER")
    print("=" * 50)

    url = input("\nEnter a URL to analyze: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed_url = urlparse(url)
    domain = parsed_url.hostname

    risk_score = 0
    reasons = []

    if parsed_url.scheme != "https":
        risk_score += 1
        reasons.append("URL does not use HTTPS")

    if len(url) > 75:
        risk_score += 1
        reasons.append("URL is unusually long")

    if "@" in url:
        risk_score += 2
        reasons.append("URL contains @ symbol")

    if domain and domain.count("-") >= 2:
        risk_score += 1
        reasons.append("Domain contains multiple hyphens")

    if domain:
        try:
            ipaddress.ip_address(domain)
            risk_score += 2
            reasons.append("URL uses an IP address instead of a domain")
        except ValueError:
            pass

    suspicious_words = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "bank",
        "password",
        "signin",
        "confirm"
    ]

    for word in suspicious_words:
        if word in url.lower():
            risk_score += 1
            reasons.append(f"Suspicious keyword detected: {word}")

    if risk_score >= 5:
        risk_level = "HIGH"
    elif risk_score >= 2:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print("\nURL Analysis")
    print("-" * 40)

    print("URL:", url)
    print("Domain:", domain)

    print("\nRisk Indicators:")

    if reasons:
        for reason in reasons:
            print("-", reason)
    else:
        print("- No obvious suspicious indicators found.")

    print("\nSuspicious Indicators:", len(reasons))
    print("Risk Score:", risk_score)
    print("Risk Level:", risk_level)

    # Save report
    report = []

    report.append("=" * 50)
    report.append("        PHISHING URL ANALYSIS REPORT")
    report.append("=" * 50)

    report.append(
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    report.append(f"URL: {url}")
    report.append(f"Domain: {domain}")
    report.append("")
    report.append(f"Suspicious Indicators: {len(reasons)}")
    report.append(f"Risk Score: {risk_score}")
    report.append(f"Risk Level: {risk_level}")
    report.append("")
    report.append("Risk Indicators:")

    if reasons:
        for reason in reasons:
            report.append(f"- {reason}")
    else:
        report.append("- No obvious suspicious indicators found.")

    report.append("")
    report.append(
        "Note: This tool uses heuristic analysis and "
        "does not guarantee that a URL is safe or malicious."
    )

    report.append("=" * 50)

    with open(
        "phishing_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("\n".join(report))

    print("\nReport saved as: phishing_report.txt")