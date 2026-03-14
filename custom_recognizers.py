from presidio_analyzer import Pattern, PatternRecognizer


# Phone Number Recognizer
class PhoneRecognizer(PatternRecognizer):

    def __init__(self, *args, **kwargs):

        patterns = [
            Pattern(
                name="phone_pattern",
                regex=r"\b03\d{9}\b",
                score=0.85
            )
        ]

        super().__init__(
            supported_entity="PHONE_NUMBER",
            patterns=patterns,
            name="PhoneRecognizer"
        )


# API Key Recognizer
class APIKeyRecognizer(PatternRecognizer):

    def __init__(self, *args, **kwargs):

        patterns = [
            Pattern(
                name="api_key_pattern",
                regex=r"sk-[A-Za-z0-9]{20,}",
                score=0.9
            )
        ]

        super().__init__(
            supported_entity="API_KEY",
            patterns=patterns,
            name="APIKeyRecognizer"
        )


# Internal ID Recognizer
class InternalIDRecognizer(PatternRecognizer):

    def __init__(self, *args, **kwargs):

        patterns = [
            Pattern(
                name="internal_id_pattern",
                regex=r"ID-\d{4}",
                score=0.85
            )
        ]

        super().__init__(
            supported_entity="INTERNAL_ID",
            patterns=patterns,
            name="InternalIDRecognizer"
        )