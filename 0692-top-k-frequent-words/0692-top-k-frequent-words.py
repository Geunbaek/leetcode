from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsCounter = Counter(words)
        wordsCounter = sorted(wordsCounter.items(), key = lambda x: (-x[1], x[0]))
        return list(map(lambda x: x[0], wordsCounter[:k]))