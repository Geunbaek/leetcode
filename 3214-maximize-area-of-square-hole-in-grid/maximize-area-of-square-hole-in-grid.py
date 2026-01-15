class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        width = 0
        height = 0
        hBars.sort()
        vBars.sort()
        
        _max = 1 if hBars else 0
        for h1, h2 in zip(hBars, hBars[1:]):
            if h2 - h1 == 1:
                _max += 1
            else:
                width = max(width, _max)
                _max = 1
        width = max(width, _max)
        
        _max = 1 if vBars else 0
        for v1, v2 in zip(vBars, vBars[1:]):
            if v2 - v1 == 1:
                _max += 1
            else:
                height = max(height, _max)
                _max = 1
        height = max(height, _max)
        print(height, width)
        return (min(height, width) + 1) ** 2