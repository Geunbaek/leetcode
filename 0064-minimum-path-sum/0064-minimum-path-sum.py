class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for y in range(1, n + 1):
            for x in range(1, m + 1):
                if x == 1:
                    dp[y][x] = dp[y - 1][x] + grid[y - 1][x - 1]
                    continue
                if y == 1:
                    dp[y][x] = dp[y][x - 1] + grid[y - 1][x - 1]
                    continue
                    
                dp[y][x] = min(dp[y - 1][x] + grid[y - 1][x - 1], dp[y][x - 1] + grid[y - 1][x - 1])
                
        for l in dp:
            print(l)
                
        return dp[-1][-1]
        