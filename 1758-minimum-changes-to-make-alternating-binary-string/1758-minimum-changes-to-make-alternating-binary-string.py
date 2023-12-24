class Solution:
    def minOperations(self, s: str) -> int:  
        def check(start):
            ret = 0
            for i in range(n):
                if i % 2 == 0 and s[i] != start:
                    ret += 1
                if i % 2 != 0 and s[i] == start:
                    ret += 1
                    
            return ret
                    
        
        n = len(s)
        
        return min(check("0"), check("1"))
        
        
        