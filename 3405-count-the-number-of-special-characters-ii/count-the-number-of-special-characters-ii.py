class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cache = ["" for _ in range(26)]

        for c in word:
            if c.islower():
                if cache[ord(c) - ord('a')] in [c, ""]:
                    cache[ord(c) - ord('a')] = c
                else:
                    cache[ord(c) - ord('a')] = None
            else:
                if cache[ord(c) - ord('A')] == c:
                    continue
                if cache[ord(c) - ord('A')] == c.lower():
                    cache[ord(c) - ord('A')] = c
                else:
                    cache[ord(c) - ord('A')] = None
                
        answer = 0
        for i in range(26):
            if cache[i] == chr(ord('a') + i).upper():
                answer += 1
        return answer