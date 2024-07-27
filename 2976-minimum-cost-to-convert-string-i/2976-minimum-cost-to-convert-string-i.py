class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def dij(start):
            h = []
            dist = [float('inf') for _ in range(26)]
            
            heapq.heappush(h, (0, start))
            
            while h:
                d, now = heapq.heappop(h)
                if dist[now] > d:
                    dist[now] = d
                    for _next, c in graph[now]:
                        if dist[_next] > c + d:
                            heapq.heappush(h, (c + d, _next))
            return dist
        
        
        n = len(original)
        graph = [[] for _ in range(26)]
        for i in range(n):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            c = cost[i]
            
            graph[u].append((v, c))
            
        cache = dict()
        answer = 0
        for u, v in zip(source, target):
            start = ord(u) - ord('a')
            if start not in cache:
                cache[start] = dij(start)
            dist = cache[start]
            end = ord(v) - ord('a')
            
            if dist[end] == float('inf'):
                return -1
            answer += dist[end]
        return answer
                
            
            