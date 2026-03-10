class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][last] 형태
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # 초기값 설정: 0만 쓰거나 1만 쓰는 경우 (limit 이하일 때만 1가지)
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # 0을 추가하는 경우
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # 연속해서 0이 limit+1개 나오는 경우를 제외
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD
                
                # 1을 추가하는 경우
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # 연속해서 1이 limit+1개 나오는 경우를 제외
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD