class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: 0}
        _sum = 0
        for i, num in enumerate(nums):
            _sum += num
            if _sum % k not in cache:
                cache[_sum % k] = i + 1
            elif cache[_sum % k] < i:
                return True
            
        return False
            
        
            
        