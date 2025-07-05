class Solution:
    def lastRemaining(self, n: int) -> int:
        l = floor(log2(n))

        answer = 1
        for i in range(l):
            if i % 2 == 0:
                answer += pow(2, i)
            else:
                if n % 2 != 0:
                    answer += pow(2, i)
            n = n // 2
        return answer