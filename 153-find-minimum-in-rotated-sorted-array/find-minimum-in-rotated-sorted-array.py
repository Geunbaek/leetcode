class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < pivot:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l % len(nums)]