class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        
        alpha = [0 for _ in range(26)]
        answer = 0
        r = 0
        for l in range(n):
            while r < n and alpha[ord(s[r]) - ord('a')] < 2:
                alpha[ord(s[r]) - ord('a')] += 1
                r += 1
            answer = max(answer, r - l)
            alpha[ord(s[l]) - ord('a')] -= 1
        return answer