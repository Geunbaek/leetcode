class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        h = []

        graph = [[] for _ in range(n)]

        for u, v, c in edges:
            graph[u].append((v, c))
            graph[v].append((u, 2 * c))

        dist = [float("inf") for _ in range(n)]
        visited = [0 for _ in range(n)]
        dist[0] = 0

        heapq.heappush(h, (0, 0))

        while h:
            now, node = heapq.heappop(h)

            if node == n - 1:
                return now
            
            if visited[node]:
                continue
            visited[node] = 1
            for _next, cost in graph[node]:
                if now + cost < dist[_next]:
                    dist[_next] = now + cost
                    heapq.heappush(h, (now + cost, _next))
        return -1