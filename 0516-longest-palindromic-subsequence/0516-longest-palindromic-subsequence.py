class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for y in range(n - 1, -1, -1):
            dp[y][y] = 1
            for x in range(y + 1, n):
                if s[y] == s[x]:
                    dp[y][x] = dp[y + 1][x - 1] + 2
                else:
                    dp[y][x] = max(dp[y + 1][x], dp[y][x - 1])

        return dp[0][n - 1]