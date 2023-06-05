class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        prevs = []
        
        for [x1, y1], [x2, y2] in zip(coordinates, coordinates[1:]):
            if x1 == x2:
                lin = 0
            elif y1 == y2:
                lin = 1
            else:
                lin = (y2 - y1) / (x2 - x1)
                
            if not prevs:
                prevs.append(lin)
                continue
            if lin != prevs[-1]:
                return False
            else:
                prevs.append(lin)
        return True
 
        
        