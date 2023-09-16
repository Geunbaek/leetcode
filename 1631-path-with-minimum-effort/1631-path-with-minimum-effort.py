import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r = len(heights)
        c = len(heights[0])
        
        h = []
        heapq.heappush(h, (0, 0, 0))
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        visited = [[float('inf') for _ in range(c)] for _ in range(r)]
        
        while h:
            max_diff, x, y = heapq.heappop(h)
   
            if x == c - 1 and y == r - 1:
                return max_diff
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                    
                diff = abs(heights[y][x] - heights[ny][nx])
                _max = max(max_diff, diff)
                
                if visited[ny][nx] <= _max:
                    continue
                    
                visited[ny][nx] = _max
                heapq.heappush(h, (_max, nx, ny))
        return 0
        