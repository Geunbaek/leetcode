class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(100)] for _ in range(100)]
        dp[0][0] = poured
        
        for y in range(99):
            for x in range(y + 1):
                if dp[y][x] > 1:
                    over = (dp[y][x] - 1) / 2
                    dp[y][x] = 1
                    dp[y + 1][x] += over
                    dp[y + 1][x + 1] += over
            
        return dp[query_row][query_glass]
                
        