class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        now = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= now:
                now = i

        return now == 0

