class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        r, c = m, n

        board = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        # count -= len(walls)
        for y, x in walls:
            board[y][x] = 1
        
        # count -= len(guards)
        for y, x in guards:
            board[y][x] = 2

        guarded = set()
        def mark(x, y):
            for nx in range(x + 1, c):
                if board[y][nx] in [1, 2]:
                    break
                board[y][nx] = 3
                guarded.add((nx, y))

            for nx in range(x - 1, -1, -1):
                if board[y][nx] in [1, 2]:
                    break
                board[y][nx] = 3
                guarded.add((nx, y))

            for ny in range(y + 1, r):
                if board[ny][x] in [1, 2]:
                    break
                board[ny][x] = 3
                guarded.add((x, ny))


            for ny in range(y - 1, -1, -1):
                if board[ny][x] in [1, 2]:
                    break
                board[ny][x] = 3
                guarded.add((x, ny))

        for y, x in guards:
            mark(x, y)

        # count -= len(guarded)

        for y in range(r):
            for x in range(c):
                if board[y][x] == 0:
                    count += 1
        return count