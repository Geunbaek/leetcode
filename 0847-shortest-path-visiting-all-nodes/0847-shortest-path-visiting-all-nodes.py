from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(i, 1 << i) for i in range(n)])
        visited = set(q)
        ans = 0
        while q:
            for _ in range(len(q)):
                u, m = q.popleft()
                if m == (1 << n) - 1:
                    return ans 
                for v in graph[u]:
                    if (v, m | 1 << v) not in visited:
                        q.append((v, m | 1 << v))
                        visited.add((v, m | 1 << v))
            ans += 1    