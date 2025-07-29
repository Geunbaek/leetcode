class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i, x in enumerate(nums):
            ans[i] = 1
            for j in range(i - 1, -1, -1):
                if (nums[j] | x) == nums[j]:
                    break
                nums[j] |= x
                ans[j] = i - j + 1
        return ans