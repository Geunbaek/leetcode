class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        h = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while h:
            cost, x, y = heappop(h)

            if x == c - 1 and y == r - 1:
                return cost

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                
                if (nx, ny) in visited:
                    continue
                
                visited.add((nx, ny))
                heappush(h, (max(cost, grid[ny][nx]), nx, ny))
        return -1

