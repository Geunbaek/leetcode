class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            result.append(nums[(i + num) % n])
        return result 