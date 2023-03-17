from collections import deque, defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(a, b, num):
            q = deque([(a, b)])
            visited[b][a] = 1
            count = 1
            edges = set()
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if grid[ny][nx] == 0:
                        edges.add((nx, ny))
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    visited[ny][nx] = 1
                    count += 1
                    q.append((nx, ny))
            for nx, ny in edges:
                memo[ny][nx][num] = max(memo[ny][nx][num], count)
            return count
            
        
        n = len(grid)
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        memo = [[defaultdict(int) for _ in range(n)] for _ in range(n)]
        visited = [[0 for _ in range(n)] for _ in range(n)]
        
        count = 0
        answer = 0
        for y in range(n):
            for x in range(n):
                if visited[y][x] == 0 and grid[y][x] == 1:
                    answer = max(answer, bfs(x, y, count))
                    count += 1
       
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 0:
                    answer = max(answer, sum(memo[y][x].values()) + 1)
        return answer
                    
                
                
                
        