class Solution:
    # bfs, topological sort
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = collections.defaultdict(list)
        indegree = collections.Counter()
        for u, v in edges:
            graph[v].append(u)
            indegree[u] += 1

        # counter[node][color]
        counter = collections.defaultdict(lambda:collections.defaultdict(int))
        q = collections.deque(filter(lambda i: indegree[i] == 0, range(n)))
        seen = 0
        ans = 0
        while q:
            node = q.popleft()
            counter[node][colors[node]] += 1
            ans = max(ans, counter[node][colors[node]])
            seen += 1
            for adj in graph[node]:
                for c in counter[node]:
                    counter[adj][c] = max(counter[adj][c], counter[node][c])
                indegree[adj] -= 1
                if indegree[adj] == 0: q.append(adj)
        
        return -1 if seen < n else ans