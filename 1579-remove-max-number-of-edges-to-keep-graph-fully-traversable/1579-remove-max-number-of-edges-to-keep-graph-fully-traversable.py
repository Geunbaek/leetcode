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
        v1 = [0 for _ in range(len(edges))]
        c1 = 0
        c2 = 0
        
        edges.sort(key = lambda x: -x[0])
        
        for i, (t, u, v) in enumerate(edges):
            if t == 2:
                continue
                
            if find(p1, u) != find(p1, v):
                union(p1, u, v)
                v1[i] = 1
                c1 += 1
        
        for i, (t, u, v) in enumerate(edges):
            if t == 1:
                continue
                
            if find(p2, u) != find(p2, v):
                union(p2, u, v)
                v1[i] = 1
                c2 += 1
                
        count = v1.count(1)
      
        if c1 != n - 1 or c2 != n - 1:
            return -1
        return len(v1) - count
        
        