class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        
        mid = n // 2
        if n % 2 == 0:
            return (nums[mid] + nums[mid - 1]) / 2
        return nums[mid]
        
        