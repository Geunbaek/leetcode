class Solution:
    def maxProduct(self, n: int) -> int:
        nums = sorted(list(map(int, str(n))))

        return nums[-1] * nums[-2]