class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1

        knowns = 0

        for day in range(1, n):
            dp[day] = knowns + dp[day - delay] - dp[day - forget]
            knowns = dp[day]

        return sum(dp[n - forget:]) % 1_000_000_007