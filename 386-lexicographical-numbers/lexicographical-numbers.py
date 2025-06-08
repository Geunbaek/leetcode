class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted([i + 1 for i in range(n)], key=lambda x: str(x))
            