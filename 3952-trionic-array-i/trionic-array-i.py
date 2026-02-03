class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        p, q = n, 0

        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                p = i
                break

        for i in range(n - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                q = i
                break

        if p - 0 < 1 or n - q <= 1 or p >= q:
            return False
        for i in range(p, q):
            if nums[i] <= nums[i + 1]:
                return False
        return True