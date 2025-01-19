class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        r, c = len(heightMap), len(heightMap[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        h = []  
        visited = [[0 for _ in range(c)] for _ in range(r)]

        for x in range(c):
            heappush(h, (heightMap[0][x], x, 0))
            visited[0][x] = 1

            heappush(h, (heightMap[r - 1][x], x, r - 1))
            visited[r - 1][x] = 1

        for y in range(1, r - 1):
            heappush(h, (heightMap[y][0], 0, y))
            visited[y][0] = 1

            heappush(h, (heightMap[y][c - 1], c - 1, y))
            visited[y][c - 1] = 1

        water = 0
        while h:
            now, x, y = heappop(h)
            _min = now
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < c and 0 <= ny < r):
                    continue

                if visited[ny][nx] == 1:
                    continue


                if heightMap[ny][nx] < _min:
                    water += _min - heightMap[ny][nx] 

                visited[ny][nx] = 1
                heappush(h, (max(heightMap[ny][nx], _min), nx, ny))

        return water
