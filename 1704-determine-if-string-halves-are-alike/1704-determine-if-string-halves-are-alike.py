import re
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        left = re.sub(r"[^aeiou]", "", s[:mid].lower())
        right = re.sub(r"[^aeiou]", "", s[mid:].lower())
        print(left, right)
        return len(list(left)) == len(list(right))
        