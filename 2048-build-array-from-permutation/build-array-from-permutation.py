class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for i, num in enumerate(nums)]
        
   