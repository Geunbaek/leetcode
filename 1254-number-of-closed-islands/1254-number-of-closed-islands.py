from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def bfs(a, b):
            q = deque([(a, b)])
            visited[b][a] = 1
            flag = True
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        flag = False
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    if grid[ny][nx] == 1:
                        continue
                    visited[ny][nx] = 1
                    q.append((nx, ny))
                    
            return flag
        
        r, c = len(grid), len(grid[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        answer = 0
        
        for y in range(r):
            for x in range(c):
                if visited[y][x] == 1 or grid[y][x] == 1:
                    continue
                result = bfs(x, y)
                if result:
                    answer += 1
                    
        return answer
        