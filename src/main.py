"""
main.py
- Runs basic tokenizer/vectorizer tests (examples)
- If UD dataset is present at /content/drive/MyDrive/UD_English-EWT/en_ewt-ud-train.conllu
  it runs additional tests on that dataset (tokenizer sample + vectorizer on first N sentences)
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer
from src.core.dataset_loaders import load_raw_text_data, load_conllu_sentences


EX_SENTENCES = [
    "Hello, world! This is a test.",
    "NLP is fascinating... isn't it?",
    "Let's see how it handles 123 numbers and punctuation!"
]

def test_tokenizers_examples():
    print("=== Test: Tokenizers on small examples ===")
    st = SimpleTokenizer()
    rt = RegexTokenizer()
    print("\n-- SimpleTokenizer --")
    for s in EX_SENTENCES:
        print(s, "->", st.tokenize(s))
    print("\n-- RegexTokenizer --")
    for s in EX_SENTENCES:
        print(s, "->", rt.tokenize(s))

def test_vectorizer_examples():
    print("\n=== Test: CountVectorizer on small corpus ===")
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]
    tokenizer = RegexTokenizer()
    vec = CountVectorizer(tokenizer)
    matrix = vec.fit_transform(corpus)
    print("Vocabulary:", vec.vocabulary_)
    print("Doc-term matrix:")
    for row in matrix:
        print(row)

UD_DIR = "/content/drive/MyDrive/UD_English-EWT"
UD_TRAIN = os.path.join(UD_DIR, "en_ewt-ud-train.conllu")

def test_tokenizers_on_ud_sample(path, sample_chars=500):
    print("\n=== Test: Tokenizers on UD sample ===")
    try:
        raw = load_raw_text_data(path)
    except FileNotFoundError:
        print(f"UD file not found at {path} — skipping UD tokenizer test.")
        return
    sample = raw[:sample_chars]
    st = SimpleTokenizer()
    rt = RegexTokenizer()
    print("Original sample (first 120 chars):", sample[:120].replace("\n"," "))
    simple_tokens = st.tokenize(sample)
    regex_tokens = rt.tokenize(sample)
    print("SimpleTokenizer tokens (first 30):", simple_tokens[:30])
    print("RegexTokenizer tokens (first 30):", regex_tokens[:30])

def test_vectorizer_on_ud(path, n_sentences=200):
    print("\n=== Test: CountVectorizer on UD (first {} sentences) ===".format(n_sentences))
    try:
        sents = load_conllu_sentences(path)
    except FileNotFoundError:
        print(f"UD file not found at {path} — skipping UD vectorizer test.")
        return
    docs = sents[:n_sentences]
    tokenizer = RegexTokenizer()
    vec = CountVectorizer(tokenizer)
    matrix = vec.fit_transform(docs)
    print("Vocabulary size:", len(vec.vocabulary_))

    inv_vocab = {i:t for t,i in vec.vocabulary_.items()}
    sample_vocab = [inv_vocab[i] for i in range(min(30, len(inv_vocab)))]
    print("Sample vocab (first 30):", sample_vocab)
    print("Doc-term matrix shape:", len(matrix), "x", (len(matrix[0]) if matrix else 0))
    if matrix:
        print("First row (first 50 cols):", matrix[0][:50])

if __name__ == "__main__":
    test_tokenizers_examples()
    test_vectorizer_examples()
    test_tokenizers_on_ud_sample(UD_TRAIN)
    test_vectorizer_on_ud(UD_TRAIN, n_sentences=200)
