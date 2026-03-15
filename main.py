# main.py
from injection_detector import detect_injection
from presidio_utils import analyze_text, anonymize_text
from policy_manager import decide_policy
import time

def measure_latency(func, *args):
    """
    Measures execution time of a function.
    Returns: (result, latency_in_seconds)
    """
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# ================= Updated Gateway Function =================
def gateway(user_input: str):
    # Step 1: Detect prompt injection
    injection_score, inj_latency = measure_latency(detect_injection, user_input)

    # Step 2: Detect PII
    analysis_results, pres_latency = measure_latency(analyze_text, user_input)

    # Count PII entities detected
    pii_count = len(analysis_results)

    # Step 3: Decide policy
    policy = decide_policy(user_input, injection_score, pii_count)

    # Step 4: Apply policy
    if policy == "ALLOW":
        output_text = user_input  # raw text
    elif policy == "MASK":
        output_text = anonymize_text(user_input, analysis_results)  # mask PII
    else:  # BLOCK
        output_text = "[INPUT BLOCKED DUE TO SECURITY RISKS]"

    # Latency info
    print(f"Injection detection latency: {inj_latency:.4f}s")
    print(f"Presidio analysis latency: {pres_latency:.4f}s")
    return output_text
# ============================================================

if __name__ == "__main__":
    print("=== LLM Security Mini-Gateway ===")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Enter text for LLM: ")
        if user_input.lower() == "exit":
            break
        output = gateway(user_input)
        print("Processed Output:", output)
        print("-" * 50)