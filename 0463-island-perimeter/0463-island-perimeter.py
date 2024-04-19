class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        answer = 0
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 0:
                    continue
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        answer += 1
                        continue
                    if grid[ny][nx] == 1:
                        continue
                    answer += 1
        return answer 
                
        
        