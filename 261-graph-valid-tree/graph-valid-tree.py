class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if p[x] != x:
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
            else:
                return False

        root = find(0)
        for i in range(1, n):
            if root != find(i):
                return False
        return True
