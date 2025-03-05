class Solution:
    def coloredCells(self, n: int) -> int:
        dp = [1]

        for i in range(1, n):
            dp.append(dp[-1] + (4 * i))
        return dp[n - 1]