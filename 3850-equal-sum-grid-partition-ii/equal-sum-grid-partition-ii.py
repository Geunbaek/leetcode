class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])

        top = defaultdict(int)
        top_total = 0

        bottom = defaultdict(int)
        bottom_total = 0

        for y in range(r):
            for x in range(c):
                bottom[grid[y][x]] += 1
                bottom_total += grid[y][x]

        for y in range(r - 1):
            for x in range(c):
                bottom[grid[y][x]] -= 1
                bottom_total -= grid[y][x]
                top[grid[y][x]] += 1
                top_total += grid[y][x]

            if bottom_total == top_total:
                return True
            
            diff = abs(top_total - bottom_total)
            top_len = y + 1
            bottom_len = r - top_len
            if top_total > bottom_total and top_len == 1 and diff in [grid[y][0], grid[y][-1]]:
                return True
            if top_total < bottom_total and bottom_len == 1 and diff in [grid[r - 1][0], grid[r - 1][-1]]:
                return True
            if top_total > bottom_total and top_len != 1:
                if c == 1:
                    if diff in [grid[0][0], grid[y][0]]:
                        return True
                else:    
                    if top[diff] != 0:
                        return True
            if top_total < bottom_total and bottom_len != 1:
                if c == 1:
                    if diff in [grid[y + 1][0], grid[-1][0]]:
                        return True
                else:    
                    if bottom[diff] != 0:
                        return True
        
        left = defaultdict(int)
        left_total = 0

        right = defaultdict(int)
        right_total = 0

        for y in range(r):
            for x in range(c):
                right[grid[y][x]] += 1
                right_total += grid[y][x]

        for x in range(c - 1):
            for y in range(r):
                right[grid[y][x]] -= 1
                right_total -= grid[y][x]
                left[grid[y][x]] += 1
                left_total += grid[y][x]

            if right_total == left_total:
                return True
            diff = abs(right_total - left_total)
            left_len = x + 1
            right_len = c - left_len
            if right_total < left_total and left_len == 1 and diff in [grid[0][x], grid[-1][x]]:
                return True
            if right_total > left_total and right_len == 1 and diff in [grid[0][c - 1], grid[-1][c - 1]]:
                return True
            if right_total < left_total and left_len != 1:
                if r == 1:
                    if diff in [grid[0][0], grid[0][x]]:
                        return True
                else:    
                    if left[diff] != 0:
                        return True
            if right_total > left_total and right_len != 1:
                if r == 1:
                    if diff in [grid[0][x + 1], grid[0][-1]]:
                        return True
                else:    
                    if right[diff] != 0:
                        return True


        return False
        
            
