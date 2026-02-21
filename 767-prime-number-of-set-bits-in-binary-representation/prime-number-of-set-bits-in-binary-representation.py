class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count_bits(num):
            return bin(num).count('1')
        
        dp = [0 for _ in range(20)]
        dp[0], dp[1] = 1, 1
        for i in range(2, 20):
            if dp[i] == 1:
                continue
            for j in range(2 * i, 20, i):
                dp[j] = 1
        answer = 0
        for num in range(left, right + 1):
            answer += 0 if dp[count_bits(num)] else 1
        return answer