class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def is_valid(x, y, size):
            return (
                0 <= x - size and 
                x + size < c and 
                0 <= y - size and
                y + size < r
            )
        def calc_size(x, y, size):
            points = set()
            tx = x
            ty = y - size
            points.add((tx, ty))

            for i in range(1, size + 1):
                points.add((tx - i, ty + i))
                points.add((tx + i, ty + i))
            
            bx = x
            by = y + size
            points.add((bx, by))
            for i in range(1, size):
                points.add((bx - i, by - i))
                points.add((bx + i, by - i))

            _sum = 0

            for nx, ny in points:
                _sum += grid[ny][nx]
            return _sum

        area = set()
        r, c = len(grid), len(grid[0])
        for y in range(r):
            for x in range(c):
                size = 0
                while is_valid(x, y, size):
                    area.add(calc_size(x, y, size))
                    size += 1
        sorted_area = sorted(area, reverse=True)
        return sorted_area[:3]
