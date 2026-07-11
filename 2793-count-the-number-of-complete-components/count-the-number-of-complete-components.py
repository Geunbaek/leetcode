class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        mst = [[] for _ in range(n)]
        p = [i for i in range(n)]
        for u, v in edges:
            union(u, v)
            mst[u].append(v)

        roots_nodes = defaultdict(int)
        roots_edges = defaultdict(int)
        for i in range(n):
            root = find(i)
            roots_nodes[root] += 1
            roots_edges[root] += len(mst[i])
        print(roots_nodes, roots_edges)
        answer = 0
        for root, nodes in roots_nodes.items():
            if nodes * (nodes - 1) / 2 == roots_edges[root]:
                answer += 1
        return answer