class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        n = len(s)
        m = len(t)
        
        right = 0
        
        for left in range(m):
            if t[left] == s[right]:
                right += 1
            if right == n:
                return True
            
        return False
        