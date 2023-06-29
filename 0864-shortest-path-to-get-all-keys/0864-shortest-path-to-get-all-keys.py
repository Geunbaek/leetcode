from collections import deque, defaultdict

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        q = deque()
        r, c = len(grid), len(grid[0])
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        visited = defaultdict(set)
        
        all_keys = 0
        
        for y in range(r):
            for x in range(c):
                grid[y] = list(grid[y])
                if grid[y][x] == "@":
                    q.append((x, y, 0, 0))
                    grid[y][x] = "."
                    visited[0].add((x, y))
                    
                if grid[y][x].islower():
                    all_keys += 1 << (ord(grid[y][x]) - ord('a'))
        
        while q:
            x, y, keys, dist = q.popleft()
            
            if keys == all_keys:
                return dist
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                    
                if grid[ny][nx] == "#":
                    continue
                    
                if (nx, ny) in visited[keys]:
                    continue
                    
                if grid[ny][nx] == '.':
                    visited[keys].add((nx, ny))
                    q.append((nx, ny, keys, dist + 1))
                    
                elif grid[ny][nx].islower():
                    new_keys = keys | (1 << (ord(grid[ny][nx]) - ord('a')))
                    visited[new_keys].add((nx, ny))
                    q.append((nx, ny, new_keys, dist + 1))
                    
                else:
                    if not (keys & (1 << (ord(grid[ny][nx]) - ord('A')))):
                        continue
                    visited[keys].add((nx, ny))
                    q.append((nx, ny, keys, dist + 1))
        return -1
       
                
            
            
    
        
        
        
        