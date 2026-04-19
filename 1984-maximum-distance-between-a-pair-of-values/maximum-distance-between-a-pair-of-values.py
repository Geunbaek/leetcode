class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        
        answer = 0

        for i in range(len(nums1)):
            while j < len(nums2) - 1 and nums1[i] <= nums2[j + 1]:
                j += 1
            if i <= j:
                answer = max(answer, j - i)
        return answer