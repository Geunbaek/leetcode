MOD = 1_000_000_007

class Fancy:
    def __init__(self):
        self.arr = []
        # 글로벌 연산 상태를 저장하는 단 두 개의 변수
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        # 새로 추가되는 값은 현재까지의 누적 연산을 무효화한 상태로 저장해야 함
        # Python 3.8+ 에서는 pow(base, -1, mod) 로 모듈러 역원을 쉽게 구할 수 있음
        inv_mul = pow(self.mul, -1, MOD) 
        original_val = ((val - self.add) * inv_mul) % MOD
        self.arr.append(original_val)

    def addAll(self, inc: int) -> None:
        # 기존 누적 덧셈에만 inc를 더해줌
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        # 곱셈은 기존 덧셈과 곱셈 모두에 영향을 미침
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        ans = (self.arr[idx] * self.mul + self.add) % MOD
        return ans