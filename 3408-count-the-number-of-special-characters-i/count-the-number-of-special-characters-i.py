class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        alpha = [[0, 0] for _ in range(26)]
        for c in word:
            if c.islower():
                alpha[ord(c) - ord('a')][0] += 1
            else:
                alpha[ord(c) - ord('A')][1] += 1
        answer = 0
        for i in range(26):
            if alpha[i][0] >= 1 and alpha[i][1] >= 1:
                answer += 1
        return answer