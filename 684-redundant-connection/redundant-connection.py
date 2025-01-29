class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        n = len(edges)
        p = [i for i in range(n + 1)]

        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
            else:
                return [u, v]

        return []