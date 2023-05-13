class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        MOD = 10 ** 9 + 7
        z, o = zero, one
        dp[z] += 1
        dp[o] += 1
        
        for i in range(high + 1):
            if i >= z:
                dp[i] += dp[i - z] % MOD
            if i >= o:
                dp[i] += dp[i - o] % MOD
        
        answer = 0
        for i in range(low, high + 1):
            answer += dp[i]
            
        return answer % MOD