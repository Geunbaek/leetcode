class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    if grid[ny][nx] == '0':
                        continue
                    visited[ny][nx] = 1
                    q.append((nx, ny))
        
        answer = 0
        r, c = len(grid), len(grid[0])
        
        visited = [[0 for _ in range(c)] for _ in range(r)]
        
        for y in range(r):
            for x in range(c):
                if visited[y][x] == 1:
                    continue
                if grid[y][x] == "0":
                    continue
                bfs(x, y)
                answer += 1
        return answer