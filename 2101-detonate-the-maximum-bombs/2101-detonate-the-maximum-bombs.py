from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def bfs(start):
            q = deque([start])
            visited = {start}
            
            while q:
                now = q.popleft()
                for _next in graph[now]:
                    if _next in visited:
                        continue
                        
                    visited.add(_next)
                    q.append(_next)
            return len(visited)
        
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                    
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = abs(x1 - x2)**2 + abs(y1 - y2)**2
                if dist <= r1** 2:
                    graph[i].append(j)
        
        answer = 0
        for i in range(n):
            answer = max(answer, bfs(i))
        return answer
        
        
        
        
        
        