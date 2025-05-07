class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        r, c = len(moveTime), len(moveTime[0])
        h = [(0, 0, 0)]
        dist = [[1_000_002_501 for _ in range(c)] for _ in range(r)]

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while h:
            cost, x, y = heappop(h)

            if dist[y][x] > cost:
                dist[y][x] = cost

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    
                    _next = max(dist[y][x], moveTime[ny][nx]) + 1
                    if dist[ny][nx] > _next:
                        heappush(h, (_next, nx, ny))

        return dist[r - 1][c - 1]
