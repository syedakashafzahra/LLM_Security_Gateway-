# injection_detector.py
INJECTION_KEYWORDS = ["ignore previous", "bypass", "malicious", "drop table", "hack"]

def detect_injection(text: str) -> int:
    """
    Simple prompt injection detector.
    Returns an integer score representing risk level (0 = safe, higher = risky).
    """
    if not isinstance(text, str):
        return 0  # Non-string input is treated as safe

    text_lower = text.lower()
    score = 0

    for keyword in INJECTION_KEYWORDS:
        if keyword in text_lower:
            score += 10  # Increment score for each risky keyword found

    return score  # Always an integer