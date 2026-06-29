class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len(list(filter(lambda x: x in word, patterns)))