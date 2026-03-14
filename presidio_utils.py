from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine

from custom_recognizers import APIKeyRecognizer, InternalIDRecognizer, PhoneRecognizer


# Initialize spaCy NLP engine
models = [{"lang_code": "en", "model_name": "en_core_web_sm"}]

nlp_engine = SpacyNlpEngine(models=models)

# Initialize Presidio analyzer
analyzer = AnalyzerEngine(nlp_engine=nlp_engine)

# Add custom recognizers
analyzer.registry.add_recognizer(APIKeyRecognizer())
analyzer.registry.add_recognizer(InternalIDRecognizer())
analyzer.registry.add_recognizer(PhoneRecognizer())

# Initialize anonymizer
anonymizer = AnonymizerEngine()


def analyze_text(text):
    return analyzer.analyze(text=text, language="en")


def anonymize_text(text, results):
    result = anonymizer.anonymize(text=text, analyzer_results=results)
    return result.text