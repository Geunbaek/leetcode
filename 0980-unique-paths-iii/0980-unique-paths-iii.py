from collections import deque

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        r = len(grid)
        c = len(grid[0])
        
        def bfs(a, b):
            q = deque()
            q.append((a, b, {(a, b)}))
            count = 0
            
            while q:
                x, y, path = q.popleft()
                if grid[y][x] == 2:
                    if len(path) == total:
                        count += 1
                    continue
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    if (nx, ny) in path:
                        continue
                    if grid[ny][nx] == -1:
                        continue
                    q.append((nx, ny, path | {(nx, ny)}))
                    
            return count
        
        total = 0
        for y in range(r):
            for x in range(c):
                if grid[y][x] != -1:
                    total += 1
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    return bfs(x, y)
                               
        return 0
                        
            
        