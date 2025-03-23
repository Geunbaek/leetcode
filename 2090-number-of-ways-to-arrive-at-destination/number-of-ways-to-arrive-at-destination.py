class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        def dij(start):
            h = [(0, start)]
            dists = [float('inf') for _ in range(n)]
            path_count = [0 for _ in range(n)]

            path_count[start] = 1
            dists[start] = 0

            while h:
                cost, now = heappop(h)

                if dists[now] < cost:
                    continue

                for _next, _cost in graph[now]:
                    if dists[_next] > cost + _cost:
                        dists[_next] = cost + _cost
                        path_count[_next] = path_count[now]
                        heapq.heappush(h, (cost + _cost, _next))
                    elif dists[_next] == cost + _cost:
                        path_count[_next] = (path_count[_next] + path_count[now]) % 1_000_000_007
            
            return dists, path_count


        graph = [[] for _ in range(n)]

        for u, v, c in roads:
            graph[u].append((v, c))
            graph[v].append((u, c))
        
        dists, path_count = dij(0)
        return path_count[n - 1]