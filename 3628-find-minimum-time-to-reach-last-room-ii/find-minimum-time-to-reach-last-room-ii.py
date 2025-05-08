class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        r, c = len(moveTime), len(moveTime[0])
        h = [(0, 0, 0, 1)]
        inf = float("inf")
        dist = [[inf for _ in range(c)] for _ in range(r)]
        visited = [[0 for _ in range(c)] for _ in range(r)]

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while h:
            cost, x, y, step = heappop(h)

            if dist[y][x] > cost:
                dist[y][x] = cost

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue

                    if visited[ny][nx]:
                        continue

                    next_cost = max(moveTime[ny][nx], cost) + step
                    visited[ny][nx] = 1
                    if dist[ny][nx] > next_cost:
                        heappush(h, (next_cost, nx, ny, 2 if step == 1 else 1))

        return dist[r - 1][c - 1]

