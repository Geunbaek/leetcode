class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        r, c = len(grid), len(grid[0])
        p = [[0 for _ in range(c)] for _ in range(r)]

        prefix = 1
        for y in range(r):
            for x in range(c):
                p[y][x] = prefix
                prefix = (prefix * grid[y][x]) % MOD

        suffix = 1
        for y in range(r - 1, -1, -1):
            for x in range(c - 1, -1, -1):
                p[y][x] = p[y][x] * suffix % MOD
                suffix = (suffix * grid[y][x]) % MOD

        return p