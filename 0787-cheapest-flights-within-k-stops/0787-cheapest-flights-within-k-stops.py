import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        visit = [0 for _ in range(n)]

        for s, e, w in flights:
            edges[s].append((w, e))

        h = [(0, src, k)]
        visit[src] += 1
        while h:
            weight, now, k = heapq.heappop(h)
            if now == dst:
                return weight
            if k >= 0:
                for w, e in edges[now]:
                    if visit[e] <= n:
                        heapq.heappush(h, (weight + w, e, k-1))
            visit[now] += 1

        return -1