from config.settings import LLM_MODEL, LLM_PROVIDER
from src.detection.detector import PhishingDetector
from src.llm.factory import create_llm_provider


def main():
    if not LLM_MODEL:
        raise ValueError(
            "LLM_MODEL is not configured."
        )

    llm = create_llm_provider(
        provider=LLM_PROVIDER,
        model=LLM_MODEL,
    )

    detector = PhishingDetector(llm)

    result = detector.analyze_email(
        subject="Urgent: Verify Your Account",
        body="""
Your account will be suspended within 24 hours.

Click the link below and enter your password
to verify your account immediately.
""",
    )

    print("\n=== Phishing Email Analysis ===\n")

    print(f"Classification: {result['classification']}")
    print(f"Risk: {result['risk']}")
    print(f"Confidence: {result['confidence']}")

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"- {reason}")


if __name__ == "__main__":
    main()