class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        r, c = len(classroom), len(classroom[0])
        visited = [[0] * c for _ in range(r)]

        sx, sy = 0, 0
        cnt = 0

        for y in range(r):
            for x in range(c):
                if classroom[y][x] == "S":
                    sx, sy = x, y
                elif classroom[y][x] == "L":
                    visited[y][x] = 1 << cnt
                    cnt += 1

        full = 1 << cnt
        bestEnergy = [
            [[-1 for _ in range(full)] for _ in range(c)] for _ in range(r)
        ]
        bestEnergy[sy][sx][0] = energy
        Info = deque()
        Info.append((sx, sy, 0, energy, 0))
        while Info:
            x, y, mask, e, steps = Info.popleft()
            if mask == full - 1:
                return steps
            if e == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                if classroom[ny][nx] == "X":
                    continue
                ne = energy if classroom[ny][nx] == "R" else e - 1
                nmask = mask | visited[ny][nx]
                if ne > bestEnergy[ny][nx][nmask]:
                    bestEnergy[ny][nx][nmask] = ne
                    Info.append((nx, ny, nmask, ne, steps + 1))
        return -1