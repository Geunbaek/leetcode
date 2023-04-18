class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        for char1, char2 in zip(word1, word2):
            answer.extend([char1, char2])
        _min = min(len(word1), len(word2))
        return "".join(answer + list(word1[_min:]) + list(word2[_min:]))
        