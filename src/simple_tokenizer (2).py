

from typing import List
import string
from src.core.interfaces import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        if not text:
            return []
        parts = text.lower().split()
        cleaned: List[str] = []
        for p in parts:

            t = p.strip(string.punctuation)
            if t:
                cleaned.append(t)
        return cleaned
