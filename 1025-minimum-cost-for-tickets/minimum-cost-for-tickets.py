class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1] + 1

        dp = [0 for _ in range(n)]
        days = set(days)
        for day in range(n):
            if day not in days:
                dp[day] = dp[day - 1]
                continue
            dp[day] = min(
                dp[max(0, day - 1)] + costs[0],
                dp[max(0, day - 7)] + costs[1],
                dp[max(0, day - 30)] + costs[2]
                )
        return dp[-1]
