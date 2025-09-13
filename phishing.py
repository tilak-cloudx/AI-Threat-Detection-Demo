import re

def check_url(url: str) -> str:
    suspicious_patterns = ["@", "//", "free", "login", "bonus", "prize"]
    if any(word in url.lower() for word in suspicious_patterns):
        return "Phishing"
    elif len(url) > 60:
        return "Suspicious"
    else:
        return "Safe"
