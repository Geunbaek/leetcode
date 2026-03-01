class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(lambda x: int(x), list(n)))