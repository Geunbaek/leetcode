class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        q = deque([k])
        ban = set([k])
        while q:
            now = q.popleft()

            for _next in graph[now]:
                if _next in ban:
                    continue
                ban.add(_next)
                q.append(_next)


        is_remove = True

        visited = set()
        for i in range(n):
            q = deque([(i, i in ban)])

            while q:
                now, is_ban = q.popleft()
                for _next in graph[now]:
                    if _next in ban:
                        is_remove &= is_ban
                    if _next in visited:
                        continue
                    visited.add(_next)
                    q.append((_next, is_ban))

        answer = [i for i in range(n)]
        if is_remove:
            return list(filter(lambda x: x not in ban, answer))
        return answer
