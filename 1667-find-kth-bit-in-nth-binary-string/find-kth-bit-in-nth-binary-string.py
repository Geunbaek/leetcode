class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(b):
            ret = ""
            for c in b:
                if c == '1':
                    ret += '0'
                else:
                    ret += '1'
            return ret
        
        def rev(b):
            return b[::-1]

        def _next(prev):
            return prev + "1" + rev(invert(prev))
        
        start = '0'

        for _ in range(n - 1):
            start = _next(start)

        return start[k - 1]