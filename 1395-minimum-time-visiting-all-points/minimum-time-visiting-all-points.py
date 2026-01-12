class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def get_dist(p1, p2):
            x, y = p1
            nx, ny = p2
            return max(abs(nx - x), abs(ny - y))
        
        dist = 0
        for p1, p2 in zip(points, points[1:]):
            dist += get_dist(p1, p2)
        return dist