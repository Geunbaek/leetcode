class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        def dfs(x, y, killed, d):
            if not (0 <= x < c and 0 <= y < r):
                return killed

            if grid[y][x] == "W":
                return killed

            if (x, y) in memo and d in memo[(x, y)]:
                return memo[(x, y)][d]
            
            memo[(x, y)] = memo.get((x, y), {})
            nx = x + dx[d]
            ny = y + dy[d]
            if grid[y][x] == "E":
                memo[(x, y)][d] = dfs(nx, ny, killed + 1, d)
            else:
                memo[(x, y)][d] = dfs(nx, ny, killed, d)
            return memo[(x, y)][d]

        r, c = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        memo = {}
        maxKilledEnemies = 0

        for y in range(r):
            for x in range(c):
                if grid[y][x] == "0":
                    killedEnemies = 0

                    for i in range(4):
                        killedEnemies += dfs(x, y, 0, i)

                    maxKilledEnemies = max(maxKilledEnemies, killedEnemies)

        return maxKilledEnemies