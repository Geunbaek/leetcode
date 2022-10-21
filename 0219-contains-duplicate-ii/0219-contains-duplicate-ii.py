from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = defaultdict(int)
        left, right = 0, 0
        
        while right < len(nums):
            while right < len(nums) and abs(right - left) <= k:
                cache[nums[right]] += 1
                if cache[nums[right]] >= 2:
                    return True
                right += 1
    
            cache[nums[left]] -= 1
            left += 1
        return False
        
            
        
        