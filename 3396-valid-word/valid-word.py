class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if re.match('^[0-9a-zA-Z]+$', word) is None:
            return False

        if not re.findall('[aeiouAEIOU]', word):
            return False

        if not re.findall('[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYX]', word):
            return False

        return True

        