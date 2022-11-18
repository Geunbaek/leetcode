import math, sys
sys.setrecursionlimit(100000)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        if n in (1, 2, 3, 5):
            return True
        
        if n % 2 == 0:
            return self.isUgly(n // 2)
        elif n % 3 == 0:
            return self.isUgly(n // 3)
        elif n % 5 == 0:
            return self.isUgly(n // 5)
        return False
            