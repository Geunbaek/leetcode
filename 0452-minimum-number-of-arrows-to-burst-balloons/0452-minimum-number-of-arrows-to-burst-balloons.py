class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        answer = 0 
        last = -float('inf')
        
        for s, e in points:
            if last < s:
                last = e
                answer += 1
                
        return answer