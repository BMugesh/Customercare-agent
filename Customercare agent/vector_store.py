import re
from collections import Counter

class VectorStore:
    def __init__(self):
        self.texts = []

    def add_texts(self, text_chunks):
        self.texts.extend(text_chunks)

    def search(self, query, k=3):
        """Simple keyword-based search as fallback"""
        query_words = set(re.findall(r'\w+', query.lower()))

        # Score each text based on keyword matches
        scores = []
        for i, text in enumerate(self.texts):
            text_words = set(re.findall(r'\w+', text.lower()))
            # Calculate simple overlap score
            overlap = len(query_words.intersection(text_words))
            scores.append((overlap, i))

        # Sort by score (descending) and return top k
        scores.sort(reverse=True)
        top_indices = [idx for _, idx in scores[:k]]

        return [self.texts[i] for i in top_indices if i < len(self.texts)]
