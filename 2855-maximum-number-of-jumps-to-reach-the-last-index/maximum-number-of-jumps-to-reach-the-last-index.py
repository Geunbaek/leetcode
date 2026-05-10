class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [0 for _ in range(n)]
        dp[0] = 1
        for y in range(n):
            for x in range(y + 1, n):
                if dp[y] == 0:
                    break
                if abs(nums[y] - nums[x]) <= target:
                    dp[x] = max(dp[y] + 1, dp[x])
        return dp[-1] - 1 if dp[-1] else -1