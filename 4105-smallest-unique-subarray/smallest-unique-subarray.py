from collections import defaultdict
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        P1, M1 = 100003, 1000000007
        P2, M2 = 100019, 1000000009

        def check(size):
            if size == 0:
                return False
                
            c = defaultdict(int)
            
            h1, h2 = 0, 0
            p1_pow, p2_pow = 1, 1
            
            for i in range(size):
                h1 = (h1 + nums[i] * p1_pow) % M1
                h2 = (h2 + nums[i] * p2_pow) % M2
                if i < size - 1:
                    p1_pow = (p1_pow * P1) % M1
                    p2_pow = (p2_pow * P2) % M2
            
            c[(h1, h2)] += 1
            
            for i in range(size, n):
                h1 = (h1 - nums[i - size]) % M1
                
        def check_hashed(size):
            if size == 0: return False
            
            p1_pow = pow(P1, size - 1, M1)
            p2_pow = pow(P2, size - 1, M2)
            
            c = defaultdict(int)
            h1, h2 = 0, 0
            
            for i in range(size):
                h1 = (h1 * P1 + nums[i]) % M1
                h2 = (h2 * P2 + nums[i]) % M2
            c[(h1, h2)] += 1
            
            for i in range(size, n):
                h1 = ((h1 - nums[i - size] * p1_pow) * P1 + nums[i]) % M1
                h2 = ((h2 - nums[i - size] * p2_pow) * P2 + nums[i]) % M2
                c[(h1, h2)] += 1
                
            for v in c.values():
                if v == 1:
                    return True
            return False

        l, r = 1, n
        ans = n

        while l <= r:
            mid = (l + r) // 2
            if check_hashed(mid):
                ans = mid      
                r = mid - 1
            else:
                l = mid + 1
                
        return ans