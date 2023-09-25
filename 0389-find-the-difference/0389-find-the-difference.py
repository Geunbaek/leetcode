from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)
        tc = Counter(t)
        
        for key in tc.keys():
            if key not in sc:
                return key
            if sc[key] != tc[key]:
                return key
        return 
        