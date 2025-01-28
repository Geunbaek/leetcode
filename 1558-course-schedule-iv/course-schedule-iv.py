class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        degrees = [0 for _ in range(numCourses)]

        graph = [[] for _ in range(numCourses)]
        path = [0 for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)
            degrees[v] += 1

        q = deque()

        for i, degree in enumerate(degrees):
            if degree == 0:
                q.append(i)

        edges = []

        while q:
            now = q.popleft()

            for _next in graph[now]:
                degrees[_next] -= 1

                if degrees[_next] == 0:
                    q.append(_next)
                    edges.append((now, _next))
                    path[_next] = path[now] + 1

        new = [[] for _ in range(numCourses)]

        for u, v in edges:
            new[u].append(v)

        answer = []
        for i, (u, v) in enumerate(queries):
            visited = [0 for _ in range(numCourses)]
            q = deque([u])
            visited[u] = 1
            while q:
                now = q.popleft()
                
                for _next in graph[now]:
                    if _next == v:
                        answer.append(True)
                        break
                    if visited[_next] == 1:
                        continue
                    visited[_next] = 1
                    q.append(_next)
                if len(answer) == i + 1:
                    break
            if len(answer) != i + 1:
                answer.append(False)
        return answer
        