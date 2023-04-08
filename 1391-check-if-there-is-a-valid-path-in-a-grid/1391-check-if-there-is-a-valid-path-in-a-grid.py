class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def bfs():
            from collections import deque
            
            q = deque([(0, 0, grid[0][0])])
            visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            visited[0][0] = 1
            
            while q:
                x, y, d = q.popleft()
                
                if x == len(grid[0]) - 1 and y == len(grid) - 1:
                    return True
                
                for xy, direct in zip(dxy[d], direction[d]):
                    nx = x + xy[0]
                    ny = y + xy[1]
            
                    if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
                        continue
                    if visited[ny][nx] == 1:
                        continue
                        
                    out = direct[1]
            
                    flag = False
                    for nd in direction[grid[ny][nx]]:
                        if nd[0] == next_direction[out]:
                            flag = True
                            
                    if not flag:
                        continue
                    
                    visited[ny][nx] = 1
                    q.append((nx, ny, grid[ny][nx]))
            return False
                    
            
        dxy = {
            1: [(1, 0), (-1, 0)],
            2: [(0, 1), (0, -1)],
            3: [(0, 1), (-1, 0)],
            4: [(1, 0), (0, 1)],
            5: [(0, -1), (-1, 0)],
            6: [(1, 0), (0, -1)]
        }
        
        direction = {
            1: [(3, 1), (1, 3)],
            2: [(0, 2), (2, 0)],
            3: [(3, 2), (2, 3)],
            4: [(2, 1), (1, 2)],
            5: [(3, 0), (0, 3)],
            6: [(0, 1), (1, 0)]
        }
        
        next_direction = {
            0: 2,
            1: 3,
            2: 0,
            3: 1
        }
        return bfs()
        
        
        