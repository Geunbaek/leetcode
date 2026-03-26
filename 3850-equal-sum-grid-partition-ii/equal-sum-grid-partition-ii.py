from collections import defaultdict
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check_split(g: List[List[int]]) -> bool:
            r, c = len(g), len(g[0])
            
            top = defaultdict(int)
            bottom = defaultdict(int)
            
            bottom_total = 0
            for row in g:
                for val in row:
                    bottom[val] += 1
                    bottom_total += val

            top_total = 0

            for y in range(r - 1):
                for val in g[y]:
                    bottom[val] -= 1
                    bottom_total -= val
                    top[val] += 1
                    top_total += val

                if bottom_total == top_total:
                    return True
                
                diff = abs(top_total - bottom_total)
                top_len = y + 1
                bottom_len = r - top_len
                
                if top_total > bottom_total:
                    if top_len == 1:
                        if diff in (g[y][0], g[y][-1]): return True
                    elif c == 1:
                        if diff in (g[0][0], g[y][0]): return True
                    elif top.get(diff, 0) > 0: 
                        return True
                        
                elif top_total < bottom_total:
                    if bottom_len == 1:
                        if diff in (g[-1][0], g[-1][-1]): return True
                    elif c == 1:
                        if diff in (g[y + 1][0], g[-1][0]): return True
                    elif bottom.get(diff, 0) > 0:
                        return True
                        
            return False

        if check_split(grid):
            return True
            
        transposed_grid = [list(col) for col in zip(*grid)]
        
        return check_split(transposed_grid)