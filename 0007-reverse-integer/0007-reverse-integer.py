class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ret = int(str(x)[::-1])
            
        else:
            ret = -int(str(x)[1:][::-1])
        
        if not (- 2 ** 31 <= ret <= 2 ** 31 - 1):
            return 0
        return ret
        