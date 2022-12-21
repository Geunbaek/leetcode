from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def check(root):
            q = deque([(root, 1)])
            visited[root] = 1
            
            while q:
                now, c = q.popleft()
                for _next in graph[now]:
                    if visited[_next] == c:
                        return False
                    if visited[_next] != 0:
                        continue
                    visited[_next] = 2 if c == 1 else 1
                    q.append((_next, 2 if c == 1 else 1))
    
            return True
        
        graph = [[] for _ in range(n + 1)]
        
        visited = [0 for _ in range(n + 1)]
        
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
                
        for i in range(n + 1):
            if visited[i] != 0:
                continue
            if not check(i):
                return False
           
        return True
        
        
        
        
        
        