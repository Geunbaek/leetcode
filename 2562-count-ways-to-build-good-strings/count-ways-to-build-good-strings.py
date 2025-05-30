class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        MOD = 10 ** 9 + 7
        dp[zero] += 1
        dp[one] += 1
        
        for i in range(high + 1):
            if i >= zero:
                dp[i] += dp[i - zero] % MOD
            if i >= one:
                dp[i] += dp[i - one] % MOD
        
        return sum(dp[low: high + 1]) % MOD