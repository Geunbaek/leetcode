class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        r, c = len(image), len(image[0])

        x1, y1 = c, r
        x2, y2 = 0, 0

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        q = deque([(y, x)])
        visited = [[0 for _ in range(c)] for _ in range(r)]

        while q:
            x, y = q.popleft()
            x1, y1 = min(x1, x), min(y1, y)
            x2, y2 = max(x2, x), max(y2, y)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue

                if visited[ny][nx]:
                    continue
                
                if image[ny][nx] != "1":
                    continue
                
                visited[ny][nx] = 1
                q.append((nx, ny))
        return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)