
from abc import ABC, abstractmethod
from typing import List

class Tokenizer(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        """Chia văn bản thành list các token"""
        raise NotImplementedError

class Vectorizer(ABC):
    @abstractmethod
    def fit(self, corpus: List[str]) -> None:
        """Xây dựng vocab từ corpus"""
        raise NotImplementedError

    @abstractmethod
    def transform(self, documents: List[str]) -> List[List[int]]:
        """Chuyển văn bản thành ma trận đặc trưng"""
        raise NotImplementedError

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """fit + transform"""
        self.fit(corpus)
        return self.transform(corpus)
