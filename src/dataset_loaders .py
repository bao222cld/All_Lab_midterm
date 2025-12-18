

from typing import List
import os

def load_raw_text_data(path: str) -> str:
    """
    Read a UD .conllu (CoNLL-U) file or plain text file and return a single string
    consisting of the FORM column tokens joined by spaces.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    parts: List[str] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) > 1:
                parts.append(cols[1])
            else:
                parts.append(line)
    return " ".join(parts)

def load_conllu_sentences(path: str) -> List[str]:
    """
    Parse a CoNLL-U file and return a list of sentences (each sentence is the joined FORM tokens).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    sents: List[str] = []
    cur: List[str] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                if cur:
                    sents.append(" ".join(cur))
                    cur = []
                continue
            if line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) > 1:
                cur.append(cols[1])
            else:
                cur.append(line)
        if cur:
            sents.append(" ".join(cur))
    return sents
