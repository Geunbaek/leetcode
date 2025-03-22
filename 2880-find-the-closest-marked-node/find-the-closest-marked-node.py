class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        def dij():
            h = []

            heappush(h, (0, s))
            dist = [float("inf") for _ in range(n)]

            while h:
                cost, now = heapq.heappop(h)

                if dist[now] > cost:
                    dist[now] = cost    

                    for _next, _cost in graph[now]:    
                        if cost + _cost < dist[_next]:
                            heapq.heappush(h, (cost + _cost, _next))

            return dist


        graph = [[] for _ in range(n)]
        for u, v, c in edges:
            graph[u].append((v, c))

        dists = dij()
        answer = float("inf")

        for mark in marked:
            answer = min(answer, dists[mark])

        if answer == float("inf"):
            return -1
        return answer

        