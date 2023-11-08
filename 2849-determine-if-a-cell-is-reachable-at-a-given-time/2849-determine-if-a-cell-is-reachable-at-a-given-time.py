class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_diff = abs(sx - fx)
        y_diff = abs(sy - fy)
        
        _min = min(x_diff, y_diff)
        _max = max(x_diff, y_diff)
        
        total = _min + (_max - _min)
        
        if x_diff == 0 and y_diff == 0 and t == 1:
            return False
        return total <= t 
        