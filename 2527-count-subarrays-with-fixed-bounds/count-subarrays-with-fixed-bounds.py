class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        min_k_index, max_k_index, left_bound = -1, -1, -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = i
                
            if num == minK:
                min_k_index = i
            if num == maxK:
                max_k_index = i
                
            answer += max(0, min(min_k_index, max_k_index) - left_bound)
        return answer