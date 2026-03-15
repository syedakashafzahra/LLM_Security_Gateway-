# LLM Security Mini-Gateway: Prompt Injection Protection and PII Security

**Name:** Syeda Kashaf Zahra
**Enrollment:** 01-134241-045
**Department:** Computer Science
**University:** Bahria University, Islamabad

---

# Overview

The **LLM Security Mini-Gateway** is a lightweight security layer designed to protect Large Language Model (LLM) applications from malicious inputs and sensitive data exposure.

The gateway works as a **pre-processing layer between the user and the LLM**. It scans incoming text to detect:

* Prompt Injection Attacks
* Personally Identifiable Information (PII)

Examples of PII include:

* Phone numbers
* Email addresses
* Personal names
* Dates or identifiers

Depending on the detected risk, the system applies one of three policies:

| Policy | Description                   |
| ------ | ----------------------------- |
| ALLOW  | Safe input is sent to the LLM |
| MASK   | Sensitive data is anonymized  |
| BLOCK  | Malicious input is blocked    |

This ensures **secure, privacy-preserving LLM interaction**.

---

# System Architecture

User Input
↓
Prompt Injection Detector
↓
PII Detector & Masker (Presidio)
↓
Policy Manager
↓
LLM Processing
↓
Logging / Analytics

The gateway acts as a **security filter before the LLM processes the input**.

---

# Project Structure

```
LLM_Security_Gateway
│
├── config.py
├── custom_recognizers.py
├── injection_detector.py
├── policy_manager.py
├── presidio_utils.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/syedakashafzahra/LLM_Security_Gateway.git
cd LLM_Security_Gateway
```

Install required libraries

```
pip install -r requirements.txt
```

---

# Usage

Run the project:

```
python main.py
```

Example input:

```
My phone number is 03001234567
```

Example output:

```
Policy: MASK
Processed Text: My phone number is ***********
```

---

# Threat Model

The gateway protects several critical assets.

| Asset                  | Sensitivity |
| ---------------------- | ----------- |
| User PII               | High        |
| LLM Response Integrity | High        |
| System Availability    | Medium      |
| Data Confidentiality   | Medium      |

---

# Supported Attack Detection

The system protects against the following attacks:

* Prompt Injection
* Data Exfiltration
* PII Exposure
* Adversarial Inputs
* Denial of Service (DoS)

---

# Evaluation Results

## Scenario-Level Testing

| Scenario         | PII Detected | Injection Score | Policy |
| ---------------- | ------------ | --------------- | ------ |
| Phone Number     | Yes          | 0               | MASK   |
| Email            | Yes          | 0               | MASK   |
| Prompt Injection | No           | 10              | BLOCK  |
| Safe Text        | No           | 0               | ALLOW  |
| Mixed PII        | Yes          | 0               | MASK   |

---

# Performance Metrics

| Module              | Average Latency |
| ------------------- | --------------- |
| Injection Detection | 0.001 seconds   |
| Presidio Analysis   | 0.08 seconds    |
| Policy Decision     | 0.0005 seconds  |

The results show **very small latency**, making the system suitable for **real-time applications**.

---

# Technologies Used

* Python
* Microsoft Presidio
* Natural Language Processing
* Security Policy Enforcement

---

# Conclusion

The **LLM Security Mini-Gateway** provides a simple but effective approach to protecting LLM systems.

It:

* Detects prompt injection attacks
* Protects user privacy by masking PII
* Applies configurable security policies
* Maintains fast processing speed

This makes it suitable for **secure deployment of LLM-based applications in real-world environments**.

---

# License

This project is created for **academic purposes** at Bahria University.
