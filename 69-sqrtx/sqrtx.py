class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x + 1):
            mul = i * i
            if mul == x:
                return i
            if mul > x:
                return i - 1
        return -1
                