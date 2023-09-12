from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        cache = defaultdict(int)
        
        for char in s:
            cache[char] += 1
           
        s = set()
        d = 0
        
        for key, val in cache.items():
            while val > 0 and val in s:
                val -= 1
                d += 1
            s.add(val)
        
        return d