class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        return max(dp)
        