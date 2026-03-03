class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(b):
            return b.replace("0", "2").replace("1", "0").replace("2", "1")
        
        def rev(b):
            return b[::-1]

        def _next(prev):
            return prev + "1" + rev(invert(prev))
        
        start = '0'

        for _ in range(n - 1):
            start = _next(start)

        return start[k - 1]