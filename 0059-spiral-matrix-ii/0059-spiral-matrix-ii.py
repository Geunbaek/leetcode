from collections import deque

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def get_path():
            q = deque([(0, 0, 0, 1)])
            visited = [[0 for _ in range(c)] for _ in range(r)]
         
            while q:
                x, y, d, num = q.popleft()
                if visited[y][x] == 0:
                    matrix[y][x] = num
                if visited[y][x] > 1:
                    return 
                visited[y][x] += 1

                nx = x + dx[d]
                ny = y + dy[d]

                if not (0 <= nx < c and 0 <= ny < r):
                    q.append((x, y, (d + 1) % 4, num))
                    continue

                if visited[ny][nx] == 1:
                    q.append((x, y, (d + 1) % 4, num))
                    continue

                q.append((nx, ny, d, num + 1))
                
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        r, c = len(matrix), len(matrix[0])
        get_path()
        return matrix
        
        
        

       