class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        r, c = len(heightMap), len(heightMap[0])

        h = []
        water = 0

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        visited = set()

        for x in range(c):
            heappush(h, (heightMap[0][x], 0, x))
            heappush(h, (heightMap[r - 1][x], r - 1, x))
            visited.add((x, 0))
            visited.add((x, r - 1))

        for y in range(r):
            heappush(h, (heightMap[y][0], y, 0))
            heappush(h, (heightMap[y][c - 1], y, c - 1))
            visited.add((0, y))
            visited.add((c - 1, y))

        while h:
            height, y, x = heappop(h)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < c and 0 <= ny < r):
                    continue

                if (nx, ny) in visited:
                    continue

                next_height = heightMap[ny][nx]

                if next_height < height:
                    water += height - next_height

                visited.add((nx, ny))
                heappush(h, (max(next_height, height), ny, nx))

        return water
