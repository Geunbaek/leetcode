class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        p = [i for i in range(n)]
        must_edges = []
        not_must_edges = []

        for u, v, s, m in edges:
            if m == 1:
                must_edges.append([u, v, s])
            else:
                not_must_edges.append([u, v, s]) 

        must_edges.sort(key = lambda x: x[2])

        answer = math.inf
        for u, v, s in must_edges:
            if find(u) != find(v):
                union(u, v)
                answer = min(answer, s)
            else:
                return -1


        not_must_edges.sort(key = lambda x: -x[2])
        q = []
        for u, v, s in not_must_edges:
            if find(u) != find(v):
                union(u, v)
                q.append(s)
                
        for i in range(min(k, len(q))):
            q[-(i + 1)] *= 2

        if q:
            answer = min(answer, min(q))
    
        root = set()
        for i in range(n):
            root.add(find(i))

        if len(root) != 1:
            return -1
        return answer
            