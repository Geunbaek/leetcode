from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        def bfs():
            q = deque()
            q.append(0)
            visited = [0 for _ in range(n)]
            visited[0] = 1
            answer = 0
            while q:
                now = q.popleft()
                for _next, check in graph[now]:
                    if visited[_next] == 1:
                        continue
                    
                    visited[_next] = 1
                    answer += check
                    q.append(_next)
                    
            return answer
        
        graph = [[] for _ in range(n)]
        
        for x, y in connections:
            graph[x].append((y, 1))
            graph[y].append((x, 0))
        return bfs()
            
        
        