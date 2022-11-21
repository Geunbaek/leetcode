from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[1], entrance[0], 0))
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        visited = set()
        
        visited.add((entrance[1], entrance[0]))
        
        while q:
            x, y, cnt = q.popleft()

            if cnt != 0 and (x == 0 or y == 0 or x == len(maze[0]) - 1 or y == len(maze) - 1):
                return cnt
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0 <= nx < len(maze[0]) and 0 <= ny < len(maze)):
                    continue
                if maze[ny][nx] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, cnt + 1))
        return -1
                    
        
        