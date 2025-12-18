

from typing import List
import re
from src.core.interfaces import Tokenizer

TOKEN_RE = re.compile(r"\.\.\.|[a-z]+(?:'[a-z]+)?|\d+|[^\w\s]", re.IGNORECASE)

class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        if not text:
            return []
        text = text.lower()
        tokens = TOKEN_RE.findall(text)

        return [t for t in tokens if t.strip() != ""]
