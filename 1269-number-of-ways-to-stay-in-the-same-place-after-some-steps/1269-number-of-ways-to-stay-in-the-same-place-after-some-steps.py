class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def find(now, depth):
            if depth <= 0:
                if now == 0:
                    return 1
                return 0
            
            ans = find(now, depth - 1)
            
            if 0 < now:
                ans += find(now - 1, depth - 1) % MOD
            if now < arrLen - 1:
                ans += find(now + 1, depth - 1) % MOD
            return ans
    
        return find(0, steps) % MOD
                
    