class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def get_dist(x1,y1,x2,y2):
            return max(abs(y2-y1),abs(x2-x1))
        ans=0
        
        n=len(points)
        x1,y1=points[0]
        for i in range(1,n):
            x2,y2=points[i]
            ans+=get_dist(x1,y1,x2,y2)
            x1,y1=x2,y2
        return ans
        