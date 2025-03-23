class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        def dij(start):
            h = [(0, start)]
            times = [float("inf") for _ in range(n)]
            paths = [0 for _ in range(n)]
            paths[start] = 1
            times[start] = 0

            while h:
                time, now = heappop(h)

                if times[now] < time:
                    continue

                for _next, cost in graph[now]:
                    if times[_next] > cost + time:
                        heappush(h, (cost + time, _next))
                        paths[_next] = paths[now]
                        times[_next] = cost + time
                    elif times[_next] == cost + time:
                        paths[_next] = (paths[_next] + paths[now]) % 1_000_000_007
            return paths[n - 1]

        graph = [[] for _ in range(n)]

        for u, v, c in roads:
            graph[u].append((v, c))
            graph[v].append((u, c))
        
        return dij(0)