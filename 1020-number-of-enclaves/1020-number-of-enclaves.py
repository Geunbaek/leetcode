class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        def bfs(a, b):
            q = deque([(a, b)])
            visited[b][a] = 1
            count = 0
            flag = True
            
            while q:
                x, y = q.popleft()
                count += 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        flag = False
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    visited[ny][nx] = 1
                    q.append((nx, ny))
            return flag, count
                    
        r, c = len(grid), len(grid[0])
        answer = 0
        visited = [[0 for _ in range(c)] for _ in range(r)]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 0 or visited[y][x] == 1:
                    continue
                flag, count = bfs(x, y)
                if flag:
                    answer += count
                    
        return answer
                