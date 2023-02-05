from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        answer = []
        p_map = dict(Counter(p))
        check = {}
        length = 0
   
        for i in range(len(s)):
            check[s[i]] = check.get(s[i], 0) + 1
            length += 1
            
            if length > len(p):
                check[s[i - len(p)]] = check.get(s[i - len(p)], 0) - 1
                if check[s[i - len(p)]] == 0:
                    del check[s[i - len(p)]]
            if p_map == check:
                answer.append(i - len(p) + 1)
        return answer
            
            
        