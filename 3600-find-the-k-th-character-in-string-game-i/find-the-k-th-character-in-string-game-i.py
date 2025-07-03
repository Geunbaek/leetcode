class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            suffix = ""

            for c in word:
                _next = ord(c) + 1

                if _next > ord('z'):
                    suffix += "a"
                else:
                    suffix += chr(_next)
            word += suffix
        return word[k - 1]