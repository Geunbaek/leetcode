from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def dij():
            dist = [float('inf') for _ in range(n)]
            ban = {0: set(), 1: set()}
            q = deque()
            
            q.append((0, 0, -1))
            
            while q:
                cost, node, prev = q.popleft()
                dist[node] = min(dist[node], cost)
                if prev == -1:
                    for _next in red_graph[node]:
                        ban[0].add(f"{node}-{_next}")
                        q.append((cost + 1, _next, 0))

                    for _next in blue_graph[node]:
                        ban[1].add(f"{node}-{_next}")
                        q.append((cost + 1, _next, 1))

                elif prev == 0:
                    for _next in blue_graph[node]:
                        if f"{node}-{_next}" in ban[1]:
                            continue
                        ban[1].add(f"{node}-{_next}")
                        q.append((cost + 1, _next, 1))
                else:
                    for _next in red_graph[node]:
                        if f"{node}-{_next}" in ban[0]:
                            continue
                        ban[0].add(f"{node}-{_next}")
                        q.append((cost + 1, _next, 0))
            return dist
                            
                        
        
        red_graph = [[] for _ in range(n)]
        blue_graph = [[] for _ in range(n)]
 
        for u, v in redEdges:
            red_graph[u].append(v)
      
        for u, v in blueEdges:
            blue_graph[u].append(v)

        dist = dij()
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
   
        return dist



            
        