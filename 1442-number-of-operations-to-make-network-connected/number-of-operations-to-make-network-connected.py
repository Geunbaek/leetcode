class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        p = [i for i in range(n)]

        cnt = 0
        for u, v in connections:
            if find(u) != find(v):
                union(u, v)
                cnt += 1
        
        remain = len(connections) - cnt
        nodes = set()
        for i in range(n):
            nodes.add(find(i))
        if len(nodes) - 1 > remain:
            return -1
        return len(nodes) - 1