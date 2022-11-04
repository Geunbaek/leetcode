class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        alpha = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        while left < right:
            while left < len(s) and s[left] not in alpha:
                left += 1

            while right >= 0 and s[right] not in alpha:
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
