class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = " " + text1
        text2 = " " + text2
        
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        
        for y in range(len(text2)):
            for x in range(len(text1)):
                if x == 0 or y == 0:
                    continue
                    
                if text1[x] == text2[y]:
                    dp[y][x] = dp[y - 1][x - 1] + 1
                else:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
                    
        return dp[-1][-1]
        