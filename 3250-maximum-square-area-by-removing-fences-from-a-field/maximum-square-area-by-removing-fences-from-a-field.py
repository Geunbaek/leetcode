class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        vMemo = set()
        MOD = 1_000_000_007
        v = [1] + vFences + [n]
        h = [1] + hFences + [m]
        v.sort()
        h.sort()

        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                vMemo.add(v[j] - v[i])
        _max = -1
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                if h[j] - h[i] in vMemo:
                    _max = max(_max, pow(h[j] - h[i], 2))
        if _max == -1:
            return _max
        return _max % MOD