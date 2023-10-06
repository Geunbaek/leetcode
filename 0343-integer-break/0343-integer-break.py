class Solution:
    def integerBreak(self, n: int) -> int:  
        @cache
        def recur(num):
            if num <= 3:
                return num
            
            ret = num
            for i in range(2, num):
                ret = max(ret, i * recur(num - i))
            return ret
        
        if n <= 3:
            return n - 1
        
        return recur(n)
                
            
                
        