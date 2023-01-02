class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.lower() == word or word.upper() == word or (word[0].isupper() and word[1:] == word[1:].lower())
        