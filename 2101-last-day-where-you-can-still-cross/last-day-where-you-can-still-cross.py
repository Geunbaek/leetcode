class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
        
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, -1, -1, -1, 0, 1, 1, 1]
        
        p = [i for i in range(row * col + 2)]
        board = [[0 for _ in range(col)] for _ in range(row)]
       
        
        for day, (a, b) in enumerate(cells):
            y, x = a - 1, b - 1
            board[y][x] = 1
            i = y * col + x + 1
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < col and 0 <= ny < row):
                    continue
                if board[ny][nx] == 0:
                    continue
                j = ny * col + nx + 1
                union(i, j)
                
            if x == 0:
                union(0, i)
            elif x == col - 1:
                union(i, row * col + 1)
                
            if find(0) == find(row * col + 1):
                return day
