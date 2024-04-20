class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            dx = [0, 1]
            dy = [1, 0]
            
            lx, ly = x, y
            while q:
                x, y = q.popleft()
                lx, ly = x, y
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    if land[ny][nx] == 0:
                        continue
                    visited[ny][nx] = 1
                    q.append((nx, ny))
            return lx, ly
        
        r, c = len(land), len(land[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        answer = []
        for y in range(r):
            for x in range(c):
                if visited[y][x] == 1:
                    continue
                if land[y][x] == 0:
                    continue
                lx, ly = bfs(x, y)
                answer.append([y, x, ly, lx])
        return answer
        