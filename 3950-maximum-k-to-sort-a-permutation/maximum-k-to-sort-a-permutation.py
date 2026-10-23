class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1

        for i, num in enumerate(nums):
            if nums[i] == i:
                continue
            res &= nums[i]
        return 0 if res == -1 else res