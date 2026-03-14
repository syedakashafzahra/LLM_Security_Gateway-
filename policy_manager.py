# policy_manager.py
INJECTION_SCORE_THRESHOLD = 5
PII_SCORE_THRESHOLD = 2  # number of PII entities before masking

def decide_policy(user_input, injection_score, pii_count):
    """
    Returns one of: "ALLOW", "MASK", "BLOCK"
    """
    try:
        score = int(injection_score)
    except (ValueError, TypeError):
        score = 0

    if score >= INJECTION_SCORE_THRESHOLD:
        return "BLOCK"
    elif pii_count > PII_SCORE_THRESHOLD:
        return "MASK"
    else:
        return "ALLOW"