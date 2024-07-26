class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dij(start):
            h = []
            
            dist = [float('inf') for _ in range(n)]
            heapq.heappush(h, (0, start))
            
            while h:
                d, now = heapq.heappop(h)
                
                if dist[now] <= d:
                    continue
                
                dist[now] = d
                for _next, cost in graph[now]:
                    if dist[_next] > d + cost:
                        heapq.heappush(h, (d + cost, _next))
            return dist
                
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def cut(x):
            if x == 0:
                return False
            
            if x > distanceThreshold:
                return False
            
            return True
        
        answer = -1
        _max = n
        
        for i in range(n):
            dist = list(filter(lambda x: cut(x),dij(i)))
            if _max >= len(dist):
                _max = len(dist)
                answer = i
        return answer
        
        
            
        