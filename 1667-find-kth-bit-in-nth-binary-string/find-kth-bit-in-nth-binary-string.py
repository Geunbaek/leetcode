class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(b):
            pattern = r"0|1"
            replacements = {"0": "1", "1": "0"}
            return re.sub(pattern, lambda m: replacements[m.group(0)], b)
        
        def rev(b):
            return b[::-1]

        def _next(prev):
            return prev + "1" + rev(invert(prev))
        
        start = '0'

        for _ in range(n - 1):
            start = _next(start)

        return start[k - 1]