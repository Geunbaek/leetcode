class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1

        node1_path = dict()
        node2_path = dict()

        graph = [[] for _ in range(len(edges))]
        indegrees = [0 for _ in range(len(edges))]
        for u, v in enumerate(edges):
            if v == -1:
                continue
            graph[u].append(v)
            indegrees[v] += 1

        q = deque([(node1, 1, 0), (node2, 2, 0)])
        node1_path[node1] = 0
        node2_path[node2] = 0
        answer = []
        while q:
            node, now, d = q.popleft()

            for _next in graph[node]:
                if now == 1:
                    if _next in node1_path:
                        continue
                    
                    if _next in node2_path:
                        answer.append((d + 1, node2_path[_next], _next))
                    node1_path[_next] = d + 1
                    q.append((_next, now, d + 1))
                else:
                    if _next in node2_path:
                        continue
                    
                    if _next in node1_path:
                        answer.append((d + 1, node1_path[_next], _next))
                    node2_path[_next] = d + 1
                    q.append((_next, now, d + 1))
        answer.sort(key = lambda x: (max(x[0], x[1]), x[2]))
        if not answer:
            return -1
        return answer[0][2]