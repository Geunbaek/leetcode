class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        
        _max, _min = nums[0], nums[0]
        cur_max, cur_min = nums[0], nums[0]
        
        for num in nums[1:]:
            cur_min = min(num, cur_min + num)
            _min = min(_min, cur_min)
            cur_max = max(num, cur_max + num)
            _max = max(_max, cur_max)
 
        return max(_max, sum(nums) - _min)
    
    