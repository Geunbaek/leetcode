class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        m = 999
        while n > m:
            answer += max(n - m, 0)
            m = (m * 1000) + 999 
        return answer