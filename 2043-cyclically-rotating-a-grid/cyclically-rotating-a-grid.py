class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def rotate(sx, sy, is_visit, is_mut):
            q = deque([(sx, sy, 0, grid[sy][sx])])
            while q:
                x, y, d, value = q.popleft()
                if d == 3 and sx == x and y == sy:
                    return
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < n and 0 <= ny < m):
                    q.append((x, y, d + 1, value))
                    continue
                if visited[ny][nx] != 0:
                    q.append((x, y, d + 1, value))
                    continue
                prev = grid[ny][nx]
                if is_visit:
                    visited[ny][nx] = 1
                if is_mut:
                    grid[ny][nx] = value
                q.append((nx, ny, d, prev))

        def calc_circum(depth):
            w = (n - (depth * 2) - 2) * 2
            h = (m - (depth * 2) - 2) * 2
            return (w + h) + 4

        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for sx, sy in zip(range(n), range(m)):
            if visited[sy][sx] != 0:
                break
            count = k % calc_circum(sx)
            for repeat in range(count):
                rotate(sx, sy, repeat == count - 1, count)
            if count == 0:
                rotate(sx, sy, 1, count)
        return grid