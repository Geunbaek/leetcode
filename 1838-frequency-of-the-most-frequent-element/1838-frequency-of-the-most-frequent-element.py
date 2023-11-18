class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        _sum = 0
            
            
        left = 0
        
        for right in range(n):
            _sum += nums[right]
            
            while (right - left + 1) * nums[right] - _sum > k:
                _sum -= nums[left]
                left += 1
            answer = max(answer, right - left + 1)
            
        return answer
                
        
