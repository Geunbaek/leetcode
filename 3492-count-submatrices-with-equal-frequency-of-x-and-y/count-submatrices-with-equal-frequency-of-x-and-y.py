class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])

        dp_x = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        dp_y = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        for y in range(1, r + 1):
            for x in range(1, c + 1):
                dp_x[y][x] = dp_x[y][x - 1] + (1 if grid[y - 1][x - 1] == "X" else 0)
                dp_y[y][x] = dp_y[y][x - 1] + (1 if grid[y - 1][x - 1] == "Y" else 0)

        for x in range(1, c + 1):
            for y in range(1, r + 1):
                dp_x[y][x] += dp_x[y - 1][x]
                dp_y[y][x] += dp_y[y - 1][x]
        answer = 0
        for y in range(1, r + 1):
            for x in range(1, c + 1):
                if x == 1 and y == 1:
                    continue
                x_cnt = dp_x[y][x]
                y_cnt = dp_y[y][x]

                if x_cnt == 0:
                    continue
                if x_cnt == y_cnt: 
                    answer += 1
        return answer