class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        visited = [[0 for _ in range(c)] for _ in range(r)]

        def check_closed(sx, sy):
            q = deque([(sx, sy)])
            visited[sy][sx] = 1
            is_closed = True
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        is_closed = False
                        continue
                    if visited[ny][nx]:
                        continue
                    if grid[ny][nx] == 1:
                        continue
                    visited[ny][nx] = 1
                    q.append((nx, ny))

            return is_closed
        answer = 0
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 0 and visited[y][x] == 0:
                    answer += check_closed(x, y)

        return answer
        

