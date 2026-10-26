class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        visited = [[0 for _ in range(c)] for _ in range(r)]

        def bfs(sx, sy):
            q = deque([(sx, sy)])
            visited[sy][sx] = 1
            
            total = 0
            while q:
                x, y = q.popleft()
                total += grid[y][x] % k

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if not (0 <= nx < c and 0 <= ny < r):
                        continue

                    if visited[ny][nx]:
                        continue

                    if grid[ny][nx] == 0:
                        continue
                
                    visited[ny][nx] = 1
                    q.append((nx, ny))
            return total
        
        answer = 0
        for y in range(r):
            for x in range(c):
                if visited[y][x] == 0 and grid[y][x] != 0:
                    answer += (bfs(x, y) % k == 0)
        return answer