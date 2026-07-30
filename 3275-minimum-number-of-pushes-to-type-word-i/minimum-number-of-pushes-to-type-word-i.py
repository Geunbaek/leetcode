class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        m = 1
        answer = 0

        while n > 8:
            answer += 8 * m
            m += 1
            n -= 8
        answer += n * m
        return answer