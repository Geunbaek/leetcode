class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        for i in range(1000, n + 1):
            answer += int(log(i, 1000))
        return answer
