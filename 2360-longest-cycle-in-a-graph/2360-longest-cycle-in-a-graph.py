from collections import deque

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def get_max_len(start):
            q = deque([start])
            visited = set([start])
            length = 0
            
            while q:
                node = q.popleft()
                length += 1
                for _next in graph[node]:
                    degree[_next] -= 1
                    if degree[_next] != 0:
                        continue
                    if _next in visited:
                        continue
                    q.append(_next)
                    
            return length
            
        answer = -1
        
        degree = [0 for _ in range(len(edges))]
        graph = [[] for _ in range(len(edges))]
        
        for i, edge in enumerate(edges):
            if edge == -1:
                continue
            degree[edge] += 1
            graph[i].append(edge)
                    
        q = deque()
        
        for i, conn in enumerate(degree):
            if conn == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            for _next in graph[node]:
                degree[_next] -= 1
                if degree[_next] == 0:
                    q.append(_next)
      
        for i in range(len(degree)):
            if degree[i] != 0:
                answer = max(answer, get_max_len(i))
        return answer
                