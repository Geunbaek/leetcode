class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = nums[0]
        for i in range(1, n):
            if nums[i] - 1 == nums[i - 1]:
                prefix += nums[i]
            else:
                break

        while prefix in nums:
            prefix += 1
        return prefix
        