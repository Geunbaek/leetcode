class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        if sum1 != sum2:
            if not zero2 and sum1 + zero1 > sum2:
                return -1
            if not zero1 and sum2 + zero2 > sum1:
                return -1
        else:
            if not zero1 and zero2:
                return -1
            if zero1 and not zero2:
                return -1

        return max(sum1 + zero1, sum2 + zero2)
        