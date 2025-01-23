class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        connect_computer = set()

        for y in range(r):
            compute = []
            for x in range(c):
                if grid[y][x] == 1:
                    compute.append((x, y))

            if len(compute) >= 2:
                for com in compute:
                    connect_computer.add(com)

        for x in range(c):
            compute = []

            for y in range(r):
                if grid[y][x] == 1:
                    compute.append((x, y))
            
            if len(compute) >= 2:
                for com in compute:
                    connect_computer.add(com)

        return len(connect_computer)