class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])

        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        for y in range(1, r + 1):
            for x in range(1, c + 1):
                dp[y][x] = dp[y][x - 1] + grid[y - 1][x - 1]

        for x in range(1, c + 1):
            for y in range(1, r + 1):
                dp[y][x] = dp[y - 1][x] + dp[y][x]
        answer = 0
        for y in range(1, r + 1):
            for x in range(1, c + 1):
                area = dp[y][x] - dp[y][0] - dp[0][x] + dp[0][0]
                if area <= k:
                    answer += 1
        return answer