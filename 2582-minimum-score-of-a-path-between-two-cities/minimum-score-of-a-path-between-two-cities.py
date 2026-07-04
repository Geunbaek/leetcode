from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def bfs():
            q = deque([1])
            visited = [0 for _ in range(n + 1)]
            
            dists = []
            
            while q:
                now = q.popleft()
                for _next, d in graph[now]:
                    dists.append(d)
                    if visited[_next] == 1:
                        continue
                    visited[_next] = 1
                    q.append(_next)
                    
            return dists
                
        
        graph = [[] for _ in range(n + 1)]
        
        for x, y, d in roads:
            graph[y].append((x, d))
            graph[x].append((y, d))
            
        return min(bfs())