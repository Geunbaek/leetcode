class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def drawLine(x, y, t):
            nx, ny = 3 * x, 3 * y
            
            dx = {
                "/": [2, 1, 0],
                "\\": [0, 1, 2]
            }
            
            dy = {
                "/": [0, 1, 2],
                "\\": [0, 1, 2]
            }
            
            for i in range(3):
                xx = nx + dx[t][i]
                yy = ny + dy[t][i]
                board[yy][xx] = 1
                
        def bfs(x, y):
            q = deque([(x, y)])
            
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]
            board[y][x] = 1
            
            while q:
                x, y = q.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if not (0 <= nx < 3 * n and 0 <= ny < 3 * n):
                        continue
                    
                    if board[ny][nx] == 1:
                        continue
        
                    board[ny][nx] = 1
                    q.append((nx, ny))
                    
        
        n = len(grid)
        
        board = [
            [0 for _ in range(3 * n)] for _ in range(3 * n)
        ]
        
        for y in range(n):
            line = grid[y]
            for x in range(n):
                if line[x] == " ":
                    continue
                drawLine(x, y, line[x])
            
        answer = 0 
        for y in range(3 * n):
            for x in range(3 * n):
                if board[y][x] == 0:
                    answer += 1
                    bfs(x, y)
        return answer