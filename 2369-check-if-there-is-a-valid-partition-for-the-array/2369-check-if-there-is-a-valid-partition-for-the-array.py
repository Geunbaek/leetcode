class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        prefix_sum = [0]
        dp = [False for _ in range(len(nums) + 1)]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
            
        dp[0] = True
 
        for i in range(2, len(nums) + 1):
            if dp[i - 2]:
                if nums[i - 1] == nums[i - 2]:
                    dp[i] = True
                    
            if i >= 3 and dp[i - 3]:
                if nums[i - 1] == nums[i - 2] and nums[i - 1] == nums[i - 3]:
                    dp[i] = True
                if nums[i -1] == nums[i - 2] + 1 and nums[i - 1] == nums[i - 3] + 2:
                    dp[i] = True
        
        return dp[-1]
            
        