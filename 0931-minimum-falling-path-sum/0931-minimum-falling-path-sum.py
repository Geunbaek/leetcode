class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0] = matrix[0]
        
        for y in range(1, r):
            for x in range(c):
                if x == 0:
                    dp[y][x] = min(dp[y-1][x], dp[y-1][x + 1]) + matrix[y][x]
                elif x == c - 1:
                    dp[y][x] = min(dp[y - 1][x], dp[y - 1][x - 1]) + matrix[y][x]
                else:
                    dp[y][x] = min(dp[y - 1][x], dp[y - 1][x - 1], dp[y - 1][x + 1]) + matrix[y][x]
                    
        return min(dp[-1])
        