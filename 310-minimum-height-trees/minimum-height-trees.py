class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        degree = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            graph[u].append(v)
            graph[v].append(u)
        leafs = set()
        q = deque()
        for i, d in enumerate(degree):
            if d == 1:
                q.append(i)
                leafs.add(i)
        depth = [0 for _ in range(n)]
        while q:
            now = q.popleft()
            for _next in graph[now]:
                if _next in leafs:
                    continue
                degree[_next] -= 1
                if degree[_next] == 1:
                    q.append(_next)
                    depth[_next] = max(depth[_next], depth[now] + 1 )
        print(depth)
                

        _max = max(depth)
        answer = []
        for i, d in enumerate(depth):
            if d == _max:
                answer.append(i)
        return answer


    

