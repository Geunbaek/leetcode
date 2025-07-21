class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy_num1 = nums1[:m]

        l, r = 0, 0

        while l < m and r < n:
            if copy_num1[l] <= nums2[r]:
                nums1[l + r] = copy_num1[l]
                l += 1
            else:
                nums1[l + r] = nums2[r]
                r += 1
        
        while l < m:
            nums1[l + r] = copy_num1[l]
            l += 1
        
        while r < n:
            nums1[l + r] = nums2[r]
            r += 1
