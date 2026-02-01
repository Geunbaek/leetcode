class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        _sum = float('inf')

        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                _sum = min(_sum, nums[i] + nums[j])
        return _sum + nums[0]