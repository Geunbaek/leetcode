class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        degrees = [0 for _ in range(numCourses)]

        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)
            degrees[v] += 1

        q = deque()

        for i, degree in enumerate(degrees):
            if degree == 0:
                q.append(i)

        prerequisites = defaultdict(set)

        while q:
            now = q.popleft()

            for _next in graph[now]:
                degrees[_next] -= 1

                prerequisites[_next].add(now)
                for p in prerequisites[now]:
                    prerequisites[_next].add(p)


                if degrees[_next] == 0:
                    q.append(_next)

        answer = []

        for u, v in queries:
            answer.append(u in prerequisites[v])
        return answer
        