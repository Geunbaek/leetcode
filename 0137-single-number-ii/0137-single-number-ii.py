from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        
        for num in nums:
            cache[num] += 1
            if cache[num] == 3:
                del cache[num]
                
        for key in cache.keys():
            if cache[key] >= 1:
                return key
        return -1
        