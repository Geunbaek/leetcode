class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(sx, sy):
            q = deque([(sx, sy)])

            visited = [[-1 for _ in range(c)] for _ in range(r)]
            visited[sy][sx] = 0

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue

                    if visited[ny][nx] != -1:
                        continue
                    
                    if grid[ny][nx] == 2:
                        continue

                    if grid[ny][nx] == 1:
                        continue

                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))
            return visited

        r, c = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        houses = []
        house_dists = {}

        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    houses.append((x, y))
                    house_dists[(x, y)] = bfs(x, y)

        answer = float("inf")
        for y in range(r):
            for x in range(c):
                if grid[y][x] != 0:
                    continue
                
                dist = 0
                for key, visited in house_dists.items():
                    if visited[y][x] != -1:
                        dist += visited[y][x]
                    else:
                        break
                else:
                    answer = min(answer, dist)

        if answer == float("inf"):
            return -1
        return answer