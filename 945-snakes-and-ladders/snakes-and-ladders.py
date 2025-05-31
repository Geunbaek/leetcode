class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        graph = [[] for _ in range(n * n + 1)]
        ladders = [-1 for _ in range(n * n + 1)]
        now = 1
        for y in range(n - 1, -1, -1):
            for x in range(n) if ((n - 1) - y) % 2 == 0 else range(n - 1, -1, -1):
                for i in range(1, 7):
                    if now + i > n * n:
                        break
                    graph[now].append(now + i)

                if board[y][x] != -1:
                    ladders[now] = board[y][x]
                now += 1


        q = deque([(1, 0)])
        visited = set([1])
        while q:
            now, count = q.popleft()

            if now >= n * n:
                return count

            for _next in graph[now]:
  
                next_pos = _next
                if ladders[_next] != -1:
                    next_pos = ladders[_next]

                if next_pos in visited:
                    continue
                visited.add(next_pos)
                q.append((next_pos, count + 1))
        return -1
