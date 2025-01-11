class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        cache = Counter(s)
        one = 0

        for key in cache.keys():
            if cache[key] % 2 != 0:
                one += 1

            if one > k:
                return False
        
        return True

        