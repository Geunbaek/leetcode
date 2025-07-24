class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[0] = 0

        for i in range(n - 1):
            diff = nums[i]

            for j in range(i + 1, i + diff + 1):
                if j >= n:
                    continue
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1]
