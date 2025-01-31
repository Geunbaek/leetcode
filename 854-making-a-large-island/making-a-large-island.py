class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(sx, sy, target):
            q = deque([(sx, sy)])
            visited[sy][sx] = target
            size = 0

            while q:
                x, y = q.popleft()
                size += 1

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue

                    if visited[ny][nx] != 0:
                        continue

                    if grid[ny][nx] == 0:
                        continue

                    visited[ny][nx] = target
                    q.append((nx, ny))
            return size

        def bfs2(sx, sy):
            q = deque([(sx, sy)])
            visited[sy][sx] = 1
            size = 1
            used = set()
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue

                    if visited[ny][nx] != 0:
                        if visited[ny][nx] != 1 and (visited[ny][nx] not in used):
                            used.add(visited[ny][nx])
                            size += size_cache[visited[ny][nx]]
                        continue

                    if grid[ny][nx] == 0:
                        continue
                    size += 1
                    q.append((nx, ny))

            return size

        r, c = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        answer = 0

        size_cache = defaultdict()
        visited = [[0 for _ in range(c)] for _ in range(r)]
        
        island_number = 2
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 0:
                    continue
                if visited[y][x] != 0:
                    continue
                size_cache[island_number] = bfs(x, y, island_number)
                island_number += 1

        print(size_cache)

        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    continue
                if visited[y][x] != 0:
                    continue
                answer = max(answer, bfs2(x, y))

        if answer == 0:
            return r * c

        return answer       

                