class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            l = max(nums[:i + 1])
            r = min(nums[i:])

            score = l - r

            if score <= k:
                return i
        return -1
