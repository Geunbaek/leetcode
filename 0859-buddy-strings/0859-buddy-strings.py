from collections import defaultdict

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            alpha = [0 for _ in range(26)]
            for c in s:
                index = ord(c) - ord('a')
                alpha[index] += 1
                if alpha[index] >= 2:
                    return True
            return False
    
        count = 0
        cache1 = defaultdict(set)        
        cache2 = defaultdict(set)

        
        for i, (c1, c2) in enumerate(zip(s, goal)):
            if c1 != c2:
                count += 1
                cache1[c1].add(i)
                cache2[c2].add(i)
                
        if len(cache1) != 2:
            return False
        
        keys = list(cache1.keys())
        
        if len(cache1[keys[0]]) != 1 or len(cache1[keys[1]]) != 1:
            return False

    
        if cache1[keys[0]] == cache2[keys[1]] and cache1[keys[1]] == cache2[keys[0]]:
            return True
        
        return False
        