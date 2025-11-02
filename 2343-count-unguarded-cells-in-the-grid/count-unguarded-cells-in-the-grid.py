class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        r, c = m, n

        board = [[-1 for _ in range(c)] for _ in range(r)]
        count = r * c
        count -= len(walls)
        for y, x in walls:
            board[y][x] = 'W'

        q = deque()

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
    
        visited = set()
        count -= len(guards)
        for y, x in guards:
            board[y][x] = 'G'
            for i in range(4):
                q.append((x, y, i))

        while q:
            x, y, d = q.popleft()
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < c and 0 <= ny < r):
                continue
            if (board[ny][nx] == 'W' or board[ny][nx] == 'G' or board[ny][nx] == d):
                continue
            visited.add((nx, ny))
            q.append((nx, ny, d))
            board[ny][nx] = d

        count -= len(visited)
        return count

