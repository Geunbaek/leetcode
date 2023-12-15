class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cache = defaultdict(list)
        
        for a, b in paths:
            cache[a].append(b)
            
        for a, b in paths:
            if b not in cache:
                return b
        
        