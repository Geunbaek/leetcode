from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def get_edges(island_id, x, y):
            edges = []
            q = deque([(x, y)])
            visited[y][x] = island_id
            
            while q:
                now_x, now_y = q.popleft()
                for i in range(4):
                    nx = now_x + dx[i]
                    ny = now_y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    if visited[ny][nx] == island_id:
                        continue
                    if grid[ny][nx] == 0:
                        edges.append((now_x, now_y))
                        continue
                    visited[ny][nx] = island_id
                    q.append((nx, ny))
                    
            return edges
        
        def get_dist(x1, y1, island_id):
            q = deque([(x1, y1, 0)])
            visited2 = [[0 for _ in range(c)] for _ in range(r)]
            visited2[y1][x1] = 1
            
            while q:
                x, y, cnt = q.popleft()
 
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    if visited2[ny][nx] == 1:
                        continue
                    if visited[ny][nx] == island_id:
                        continue
                    if visited[ny][nx] != float("inf") and visited[ny][nx] != island_id:
                        return cnt
                    visited2[ny][nx] = 1
                    q.append((nx, ny, cnt + 1))
            return float('inf')
        
        island_id = 1
        r, c = len(grid), len(grid[0])
        visited = [[float('inf') for _ in range(c)] for _ in range(r)]
        answer = float('inf')
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        edge_cache = {}     
    
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 0 or visited[y][x] <= island_id:
                    continue
                edge_cache[island_id] = get_edges(island_id, x, y)
                island_id += 1
            
        for x1, y1 in edge_cache[1]:
            for x2, y2 in edge_cache[2]:
                answer = min(answer, abs(y2 - y1) + abs(x2 - x1) - 1)
            # answer = min(answer, get_dist(x1, y1, 1))
    
        return answer
        
                
                    
                
            
        