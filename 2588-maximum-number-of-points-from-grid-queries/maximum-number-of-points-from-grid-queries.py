class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        answer = [0 for _ in range(len(queries))]

        
        r, c = len(grid), len(grid[0])

        h = [(grid[0][0], 0, 0)]
        visited = [[0 for _ in range(c)] for _ in range(r)]
        visited[0][0] = 1
        visited_cells = 0

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        thresholds = [0 for _ in range(r * c + 1)]
        while h:
            max_value, x, y = heappop(h)
            visited_cells += 1
            thresholds[visited_cells] = max_value
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                
                if visited[ny][nx]:
                    continue

                visited[ny][nx] = 1
                heappush(h, (max(max_value, grid[ny][nx]), nx, ny))
        
        for i, query in enumerate(queries):
            left, right = 0, r * c

            while left <= right:
                mid = (left + right) // 2
                if thresholds[mid] < query:
                    left = mid + 1
                else:
                    right = mid - 1
            answer[i] = right

        return answer
