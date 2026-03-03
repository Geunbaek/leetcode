class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(b):
            table = str.maketrans('01', '10')
            return b.translate(table)
        
        def rev(b):
            return b[::-1]

        def _next(prev):
            return prev + "1" + rev(invert(prev))
        
        start = '0'

        for _ in range(n - 1):
            start = _next(start)

        return start[k - 1]