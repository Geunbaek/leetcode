class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @cache
        def recur(depth):
            if depth >= n:
                return 1
        
            ret = 0
            
            if depth + 1 <= n:
                if not (1 <= int(s[depth]) <= 9):
                    ret += 0 
                else:
                    ret += recur(depth + 1)
            
            if depth + 2 <= n:
                if not (10 <= int(s[depth: depth + 2]) <= 26):
                    ret += 0
                else:
                    ret += recur(depth + 2)
            
            return ret
        return recur(0)
            
            
            
        
        alphabet_map = {
            i + 1: chr(ord('A') + i) for i in range(26)
        }
        
        print(alphabet_map)
        