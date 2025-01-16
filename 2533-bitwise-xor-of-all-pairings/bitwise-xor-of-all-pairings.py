class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        xor2 = 0

        if len(nums2) % 2 != 0:
            for n1 in nums1:
                xor1 ^= n1

        if len(nums1) % 2 != 0:
            for n2 in nums2:
                xor2 ^= n2

        return xor1 ^ xor2