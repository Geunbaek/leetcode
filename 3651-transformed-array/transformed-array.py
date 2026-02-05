class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + num) % len(nums)] for i, num in enumerate(nums)]