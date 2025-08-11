import difflib
from typing import Optional

def exact_match(predicted: str, expected: Optional[str]) -> bool:
    """Return True if predicted matches expected exactly."""
    if expected is None:
        return False
    return predicted.strip() == expected.strip()

def levenshtein_similarity(predicted: str, expected: Optional[str]) -> float:
    """Return a similarity score between 0 and 1 using difflib."""
    if expected is None:
        return 0.0
    return difflib.SequenceMatcher(None, predicted.strip(), expected.strip()).ratio()
