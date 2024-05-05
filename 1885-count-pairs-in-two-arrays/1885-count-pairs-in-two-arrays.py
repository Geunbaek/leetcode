class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        answer = 0
        diff = [nums1[i] - nums2[i] for i in range(n)]
        diff.sort()
        
        for i in range(n):
            if diff[i] > 0:
                answer += n - i - 1
            else:
                left = i + 1
                right = n - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    if diff[i] + diff[mid] > 0:
                        right = mid - 1
                    else:
                        left = mid + 1
                answer += n - left
                
        return answer
            
            