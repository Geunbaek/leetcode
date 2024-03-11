class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cache = dict()
        
        for i, c in enumerate(order):
            cache[c] = i
            
        ans = sorted(list(s), key = lambda x: cache[x] if x in cache else ord(x))
        return "".join(ans)
        