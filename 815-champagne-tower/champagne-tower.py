class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[poured]]

        for y in range(1, query_row + 1):
            dp.append([0 for _ in range(y + 1)])
            for x in range(y):
                if dp[y - 1][x] > 1:
                    overflow = dp[y - 1][x] - 1
                    dp[y][x] += overflow / 2
                    dp[y][x + 1] += overflow / 2

        if dp[query_row][query_glass] >= 1:
            return 1
        return dp[query_row][query_glass]