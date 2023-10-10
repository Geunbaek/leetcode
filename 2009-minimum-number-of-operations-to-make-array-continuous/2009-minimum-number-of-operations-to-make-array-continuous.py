class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        nums = sorted(set(nums))
        answer = n - 1
        
        for i in range(len(nums)):
            target = nums[i] + n - 1
            
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
            count = left - i
            answer = min(answer, n - count)
 
        return answer
        