import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        
        for num in range(1, int(math.sqrt(n)) + 1):
            for i in range(num ** 2, n + 1):
                dp[i] = min(dp[i] , dp[i - (num ** 2)] + 1)

        return dp[n]         
        