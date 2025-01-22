class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        r, c = len(isWater), len(isWater[0])

        q = deque()

        answer = [[0 for _ in range(c)] for _ in range(r)]
        visited = [[0 for _ in range(c)] for _ in range(r)]
        
        for y in range(r):
                for x in range(c):
                    if (isWater[y][x] == 1): 
                        q.append((x, y, 0))
                        visited[y][x] = 1

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
    
        while q:
            x, y, count = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < c and 0 <= ny < r):
                    continue

                if visited[ny][nx] != 0:
                    continue

                visited[ny][nx] = 1
                answer[ny][nx] = count + 1
                q.append((nx, ny, count + 1))
        return answer 
            


         