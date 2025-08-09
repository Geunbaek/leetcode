class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        value = math.log2(n)
        return value == math.floor(value)