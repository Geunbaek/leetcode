from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def getDist(lands):
            q = deque()
            visited = [[0 for _ in range(n)] for _ in range(n)]
            
            for land in lands:
                x, y = land
                q.append((x, y))
                
            dist = -1
            while q:
                length = len(q)
                while length:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                        if visited[ny][nx] == 1:
                            continue
                        visited[ny][nx] = 1
                        q.append((nx, ny))
                        
                    length -= 1
                dist += 1
            return dist
                    
            
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        lands = []
        n = len(grid)
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 1:
                    lands.append((x, y))
                    
        if not lands or len(lands) == n * n:
            return -1
        
        return getDist(lands)
                    
  
                        
        