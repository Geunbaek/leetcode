class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((i, j, abs(x1 - x2) + abs(y1 - y2)))
                
        edges.sort(key = lambda x: x[-1])
        p = [i for i in range(n)]
        
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
                
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        answer = 0
        connect = 0
        for u, v, d in edges:
            if find(u) != find(v):
                union(u, v)
                answer += d
                connect += 1
                
            if connect == n - 1:
                break
                
        return answer