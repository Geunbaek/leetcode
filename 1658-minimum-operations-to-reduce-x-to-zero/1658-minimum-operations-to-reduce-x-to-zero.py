class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def check_valid_range(left, right):
            if left <= len(nums) <= right:
                return True
        
            return False
        expand_nums = nums * 2
        n = len(expand_nums)
        
        prefix = [0]
        
        for i in range(n):
            prefix.append(prefix[-1] + expand_nums[i])
            
        right = 0
        answer = float('inf')
  
        for left in range(n + 1):
            while right + 1 < n and prefix[right] - prefix[left] < x:
                right += 1
            
            if prefix[right] - prefix[left] == x and right - left <= len(nums) and check_valid_range(left, right):
                answer = min(answer, right - left)
        
        if answer == float('inf'):
            return -1
        
        return answer
            
        