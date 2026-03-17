import time
from injection_detector import detect_injection
from policy_manager import decide_policy
from analyzer_setup import analyze_text, anonymize_text


def process_input(user_input: str):
    start_time = time.time()

    # Step 1: Injection Detection
    injection_score = detect_injection(user_input)

    # Step 2: PII Detection
    analysis_results = analyze_text(user_input)
    pii_count = len(analysis_results)

    # Step 3: Policy Decision
    decision = decide_policy(user_input, injection_score, pii_count)

    # Step 4: Apply Policy
    if decision == "BLOCK":
        output = "[BLOCKED]"
    elif decision == "MASK":
        output = anonymize_text(user_input, analysis_results)
    else:
        output = user_input

    latency = round((time.time() - start_time) * 1000, 2)

    return {
        "input": user_input,
        "injection_score": injection_score,
        "pii_count": pii_count,
        "decision": decision,
        "output": output,
        "latency_ms": latency
    }


def main():
    while True:
        user_input = input("\nEnter text (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        result = process_input(user_input)

        print("\n=== RESULT ===")
        for k, v in result.items():
            print(f"{k}: {v}")


if __name__ == "__main__":
    main()