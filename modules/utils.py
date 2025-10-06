import re
from collections import Counter

STOPWORDS = {
    "DE": {"und", "oder", "aber", "nicht", "der", "die", "das", "ein", "eine"},
    "EN": {"and", "or", "but", "not", "the", "a", "an"},
    "FR": {"et", "ou", "mais", "pas", "le", "la", "les", "un", "une"},
    "ES": {"y", "o", "pero", "no", "el", "la", "los", "una"},
    "IT": {"e", "o", "ma", "non", "il", "la", "un"},
    "PT": {"e", "ou", "mas", "não", "o", "a", "um", "uma"}
}

def summarize_local_text(text: str, language="DE") -> str:
    text = re.sub(r"[^a-zA-ZäöüÄÖÜß ]", "", text.lower())
    words = text.split()
    words = [w for w in words if w not in STOPWORDS.get(language, set())]
    counts = Counter(words)
    if not counts:
        return "Keine aussagekräftige Zusammenfassung möglich."
    top_words = [w for w, _ in counts.most_common(5)]
    return f"Top-Themen ({language}): " + ", ".join(top_words)
