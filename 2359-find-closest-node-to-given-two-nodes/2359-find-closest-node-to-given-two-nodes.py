from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = [[] for _ in range(n)]
        dist = {i: [-1, -1] for i in range(n)}
        
        for i, edge in enumerate(edges):
            if edge == -1:
                continue
            graph[i].append(edge)
            
            
        def bfs(start, target):
            q = deque([(start, 0)])
            
            visited = [0 for _ in range(n)]
            visited[start] = 1
            
            while q:
                now, d = q.popleft()
                dist[now][target] = d
                
                for _next in graph[now]:
                    if visited[_next] == 1:
                        continue
                    visited[_next] = 1
                    q.append((_next, d + 1))
                    
        bfs(node1, 0)
        bfs(node2, 1)
        min_dist = float("inf")
        answer = float("inf")
        for key, val in dist.items():
            d1, d2 = val
 
            if d1 == -1 or d2 == -1:
                continue
            if min_dist > max(d1, d2):
                min_dist = max(d1, d2)
                answer = key
            elif min_dist == max(d1, d2) and answer > key:
                answer = key
                
        return -1 if answer == float('inf') else answer
                    
            
                
                            
    
            
            
            
        