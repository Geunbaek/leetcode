class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        reversed_operation = []

        for i in range(len(operations), 0, -1):
            mid = pow(2, i - 1)
            if (k - 1) >= mid:
                reversed_operation.append(operations[i - 1])
                k -= mid
        word = "a"
        for op in reversed(reversed_operation):
            if op == 1:
                word = chr(ord(word) + 1)
            
            if ord(word) > ord('z'):
                word = 'a'

        return word