class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#" for _ in range(n)] for _ in range(m)]
        
        for x in range(n):
            grid[0][x] = '.'

        for y in range(m):
            grid[y][-1] = '.'

        ret = []

        for y in range(m):
            ret.append("".join(grid[y]))
        return ret
            