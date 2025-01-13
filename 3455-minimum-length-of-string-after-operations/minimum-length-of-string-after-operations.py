class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        alpha = [chr(ord('a') + i) for i in range(26)]

        for char in alpha:
            count = s.count(char)
            while count >= 3:
                count -= 2
                n -= 2
        return n
