class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        p = [i for i in range(n + 1)]
        connections.sort(key=lambda x:x[-1])
        total = 0

        for u, v, c in connections:
            if find(u) != find(v):
                union(u, v)
                total += c
        
        roots = set()
        for i in range(1, n + 1):
            roots.add(find(i))

        if len(roots) == 1:
            return total
        return -1

