class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        for i in range(1000, n + 1):
            l = len(str(i))
            answer += (l - 1) // 3
        return answer
