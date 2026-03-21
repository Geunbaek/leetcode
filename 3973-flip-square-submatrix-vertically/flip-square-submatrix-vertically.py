class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        x, y = y, x
        i = 1
        for ny in range(y, y + (k // 2)):
            for nx in range(x, x + k):
                grid[ny][nx], grid[y + k - i][nx] = grid[y + k - i][nx], grid[ny][nx]
            i += 1
        return grid