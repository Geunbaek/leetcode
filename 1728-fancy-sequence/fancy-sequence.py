MOD = 1_000_000_007

class Fancy:
    def __init__(self):
        self.arr = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        inv_mul = pow(self.mul, -1, MOD) 
        original_val = ((val - self.add) * inv_mul) % MOD
        self.arr.append(original_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        ans = (self.arr[idx] * self.mul + self.add) % MOD
        return ans