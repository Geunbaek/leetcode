class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        
        answer = []
        
        for key, num in nums1.items():
            for _ in range(num):
                if key in nums2:
                    nums2[key] -= 1
                    answer.append(key)
                if nums2[key] == 0:
                    del nums2[key]
                    
        return answer
            
            