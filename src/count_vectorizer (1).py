
from typing import List, Dict
from src.core.interfaces import Vectorizer, Tokenizer

class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.vocabulary_: Dict[str, int] = {}

    def fit(self, corpus: List[str]) -> None:
        tokens = set()
        for doc in corpus:
            tokens.update(self.tokenizer.tokenize(doc))

        self.vocabulary_ = {tok: i for i, tok in enumerate(sorted(tokens))}

    def transform(self, documents: List[str]) -> List[List[int]]:
        if not self.vocabulary_:
            raise ValueError("Vocabulary is empty. Call fit() first.")
        vectors: List[List[int]] = []
        for doc in documents:
            vec = [0] * len(self.vocabulary_)
            for t in self.tokenizer.tokenize(doc):
                if t in self.vocabulary_:
                    vec[self.vocabulary_[t]] += 1
            vectors.append(vec)
        return vectors
