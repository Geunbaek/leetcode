class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cache = {
            "G": [0, 0],
            "P": [0, 0],
            "M": [0, 0]
        }
        
        for c in "GPM":
            g = garbage[0]
            counter = Counter(g)
            cache[c][0] += counter[c]
        
        for i, g in enumerate(garbage):
            if i == 0:
                continue
     
            counter = Counter(g)
            for c in "GPM":    
                cache[c][1] += travel[i - 1]
                cache[c][0] += counter[c]
                if counter[c] != 0:
                    cache[c][0] += cache[c][1]
                    cache[c][1] = 0
       
        _sum = 0

        for c in "GPM":
            _sum += cache[c][0]
        return _sum
                 
        