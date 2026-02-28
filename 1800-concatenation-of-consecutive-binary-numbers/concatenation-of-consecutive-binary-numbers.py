class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1_000_000_007
        s = "".join(map(lambda x: bin(x % MOD)[2:], range(1, n + 1)))
        return int(s, 2) % MOD