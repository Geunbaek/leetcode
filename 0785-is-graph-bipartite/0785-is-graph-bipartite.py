from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(s):
            q = deque([(s, 1)])
            visited[s] = 1
            
            while q:
                now, c = q.popleft()
                for _next in graph[now]:
                    if visited[_next] == c:
                        return False
                    if visited[_next] != 0:
                        continue
                    visited[_next] = 1 if c == 2 else 2
                    q.append((_next, 1 if c == 2 else 2))
        
            return True
            

        n = len(graph)
        visited = [0 for _ in range(n)]
        
        answer = True
        for i in range(n):
            if visited[i] != 0:
                continue
            result = bfs(i)
            answer &= result
 
        return answer
            
        