class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        _max = 0
        for i in range(n // 2):
            _max = max(_max, nums[i] + nums[n - i - 1])
        return _max
            
        