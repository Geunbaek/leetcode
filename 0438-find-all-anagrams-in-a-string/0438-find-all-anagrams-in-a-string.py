from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        answer = []
        p_map = Counter(p)
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i: i + len(p)]) == p_map:
                answer.append(i)
                
        return answer
            
            
        