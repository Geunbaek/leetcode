from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        counter = Counter(s1)
        
        for i in range(len(s2) - n + 1):
            if Counter(s2[i: i + n]) == counter:
                return True
        return False
            
    
        