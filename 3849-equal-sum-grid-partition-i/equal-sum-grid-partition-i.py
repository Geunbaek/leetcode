class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])

        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        for y in range(1, r + 1):
            for x in range(1, c + 1):
                dp[y][x] = dp[y][x - 1] + grid[y - 1][x - 1]

        for x in range(1, c + 1):
            for y in range(1, r + 1):
                dp[y][x] += dp[y - 1][x]

        for pivot in range(1, c):
            left = dp[-1][pivot]
            right = dp[-1][-1] - dp[-1][pivot]
            if left == right:
                return True
        
        for pivot in range(1, r):
            top = dp[pivot][-1]
            bottom = dp[-1][-1] - dp[pivot][-1]
            if top == bottom:
                return True
        return False
        