class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l, r = 0, 1_000_000_001

        def get_area(line):
            area = [0, 0]

            for x, y, l in squares:
                if y < line and line < y + l:
                    area[0] += l * (line - y)
                    area[1] += l * (y + l - line)
                    continue
                if line <= y:
                    area[1] += l * l
                else:
                    area[0] += l * l
            return area
        EPSILON = 1e-5
        while r - l > EPSILON:
            mid = (l + r) / 2
            up, down = get_area(mid)
            if down <= up:
                r = mid
            else:
                l = mid
        return l
                
