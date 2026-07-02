class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        r, c = len(grid), len(grid[0])
        q = deque()
        visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(health + 1)]
    
        if grid[0][0] == 1:
            q.append((0, 0, health - 1))
            visited[health - 1][0][0] = 1
        else:
            q.append((0, 0, health))
            visited[health][0][0] = 1
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        while q:
            x, y, h = q.popleft()
            if y == r - 1 and x == c - 1 and h >= 1:
                return True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                if grid[ny][nx] == 1:
                    if h <= 0:
                        continue
                    if visited[h - 1][ny][nx] == 1:
                        continue
                else:
                    if visited[h][ny][nx] == 1:
                        continue
                if grid[ny][nx] == 1:
                    if h <= 0:
                        continue
                    visited[h - 1][ny][nx] = 1
                    q.append((nx, ny, h - 1))
                else:
                    visited[h][ny][nx] = 1
                    q.append((nx, ny, h))

        return False
