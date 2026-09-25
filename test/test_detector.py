from src.detection.detector import PhishingDetector


class FakeLLM:

    def generate(self, prompt: str) -> str:

        return """
        {
            "classification": "phishing",
            "risk": "high",
            "confidence": 0.95,
            "reasons": [
                "The email creates urgency.",
                "The email requests a password."
            ]
        }
        """


def test_detector():

    detector = PhishingDetector(FakeLLM())

    result = detector.analyze_email(
        subject="Urgent account verification",
        body="Enter your password immediately.",
    )

    assert result["classification"] == "phishing"
    assert result["risk"] == "high"

    assert (
        0.0
        <= result["confidence"]
        <= 1.0
    )

    assert len(result["reasons"]) > 0