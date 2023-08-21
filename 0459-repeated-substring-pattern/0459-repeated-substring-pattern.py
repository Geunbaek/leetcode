class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(start, interval, prev):
            if start >= len(s):
                return True
            if prev == s[start:start+interval]:
                return check(start + interval, interval, prev)
            else:
                return False
        
        for i in range(1, len(s)):
            if len(s) % i != 0:
                continue
            if check(0, i, s[0:i]):
                return True
            
        return False
            