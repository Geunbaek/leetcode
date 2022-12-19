class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
    
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        p = [i for i in range(n)]
        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
                
        return find(source) == find(destination)