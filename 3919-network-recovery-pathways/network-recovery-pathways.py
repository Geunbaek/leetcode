class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:     
        def can_go(limit):
            h = [(0, 0)]
            dist = [float('inf') for _ in range(n)]

            while h:
                cost, now = heapq.heappop(h)
                if now == n - 1:
                    return True

                if dist[now] > cost:
                    dist[now] = cost

                    for _next, w in graph[now]:
                        if cost + w > k:
                            continue
                        if w < limit:
                            continue
                        if dist[_next] > cost + w:
                            heapq.heappush(h, (cost + w, _next))
            return False

        
        n = len(online)

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            graph[u].append((v, w))

        l, r = 0, 100_000 * 1_000_000_000
        while l <= r:
            mid = (l + r) // 2
            if can_go(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r if r >= 0 else -1