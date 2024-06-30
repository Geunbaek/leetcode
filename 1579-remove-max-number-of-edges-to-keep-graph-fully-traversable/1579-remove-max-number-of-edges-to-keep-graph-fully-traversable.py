class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(p, x):
            if p[x] != x:
                p[x] = find(p, p[x])
            return p[x]
        
        def union(p, a, b):
            ap = find(p, a)
            bp = find(p, b)
            p[ap] = bp
            
        
        p1 = [i for i in range(n + 1)]
        p2 = [i for i in range(n + 1)]
        c = len(edges)
        edges.sort(reverse=True)
        
        for t, u, v in edges:
            if t == 3:
                if find(p1, u) != find(p1, v) and find(p2, u) != find(p2, v):
                    union(p1, u, v)
                    union(p2, u, v)
                    c -= 1
            if t == 2:
                if find(p2, u) != find(p2, v):
                    union(p2, u, v)
                    c -= 1
            if t == 1:
                if find(p1, u) != find(p1, v):
                    union(p1, u, v)
                    c -= 1
        
        root1 = find(p1, 1)
        root2 = find(p2, 1)
        
        for i in range(2, n + 1):
            if root1 != find(p1, i):
                return -1
            if root2 != find(p2, i):
                return -1
        
        return c
        