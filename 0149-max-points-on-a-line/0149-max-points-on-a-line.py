from collections import defaultdict
def getGradient(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    
    if x1 == x2:
        return 1
    if y1 == y2:
        return 0
    return (y1 - y2) / (x1 - x2), 

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        answer = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                gradient = getGradient(points[i], points[j])
                count = 0
                for z in range(len(points)):
                    if i == z or j == z:
                        continue
                    if getGradient(points[i], points[z]) == gradient:
                        count += 1
                answer = max(answer, count + 2)
                         
        return answer
                
        