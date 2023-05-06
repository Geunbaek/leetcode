class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0
        mod = 10 ** 9 + 7
        
        for i in range(len(nums)):
            left, right = i, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            if right < i:
                continue
            answer += pow(2, right - i, mod)
        
        return answer % mod
  
        
        