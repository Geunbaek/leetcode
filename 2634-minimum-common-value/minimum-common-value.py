class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num2_set = set(nums2)

        nums1.sort()
        for num in nums1:
            if num in num2_set:
                return num
        return -1