class Solution:
    def countOrders(self, n: int) -> int:
        return math.factorial(n * 2) // (2 ** n) % 1_000_000_007