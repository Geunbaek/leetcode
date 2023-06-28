import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        
        for (u, v), d in zip(edges, succProb):
            graph[u].append((v, d))
            graph[v].append((u, d))
            
        def dij():
            h = []
            heapq.heappush(h, (-1.0, start))
            
            dist = [0.0 for _ in range(n)]
            
            while h:
                cur_dist, now = heapq.heappop(h)
                if now == end:
                    return -cur_dist
                
                dist[now] = -cur_dist
                
                for _next, cost in graph[now]:
                    if dist[_next] < cur_dist * -cost:
                        heapq.heappush(h, (cur_dist * cost, _next))
            return 0.0
        
        return dij()