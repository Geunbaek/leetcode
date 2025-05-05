class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0 for _ in range(1001)]
        MOD = 1_000_000_007

        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]
            dp[i] %= MOD

        return dp[n]