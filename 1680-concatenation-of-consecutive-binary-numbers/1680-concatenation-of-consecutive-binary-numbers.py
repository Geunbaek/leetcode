class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = ""
        for i in range(1, n + 1):
            binary += bin(i)[2:]
    
        return int(binary, 2) % 1_000_000_007