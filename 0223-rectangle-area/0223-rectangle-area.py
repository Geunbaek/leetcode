def getRange(ax1, ax2, bx1, bx2):
    if ax1 <= bx1 <= bx2 <= ax2: 
        return bx2 - bx1
    if ax1 <= bx1 <= ax2 <= bx2:
        return ax2 - bx1
    if bx1 <= ax1 <= bx2 <= ax2:
        return bx2 - ax1
    if bx1 <= ax1 <= ax2 <= bx2:
        return ax2 - ax1
    return 0

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = (ax2 - ax1) * (ay2 - ay1)
        rect2 = (bx2 - bx1) * (by2 - by1)
        rect3 = getRange(ax1, ax2, bx1, bx2) * getRange(ay1, ay2, by1, by2)
        
        return rect1 + rect2 - rect3
        