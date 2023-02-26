class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2
        
        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
        
        for i in range(len(word1)):
            dp[0][i] = i
            
        for i in range(len(word2)):
            dp[i][0] = i
            
        for y in range(1, len(word2)):
            for x in range(1, len(word1)):
                if word1[x] != word2[y]:
                    dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
                else:
                    dp[y][x] = dp[y - 1][x - 1]
                    
        return dp[-1][-1]