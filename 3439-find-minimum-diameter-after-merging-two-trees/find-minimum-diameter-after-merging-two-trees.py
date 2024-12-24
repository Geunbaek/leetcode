class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = self.get_graph(edges1)
        graph2 = self.get_graph(edges2)

        diameter1 = self.find_diameter(n, graph1)
        diameter2 = self.find_diameter(m, graph2)

        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, combined_diameter)

    def get_graph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def find_diameter(self, n, graph):
        q = deque()
        degrees = [len(graph[i]) for i in range(n)]

        for node in range(n):
            if degrees[node] == 1:
                q.append(node)

        remaining_nodes = n
        leaves_layers_removed = 0

        while remaining_nodes > 2:
            size = len(q)
            remaining_nodes -= size
            leaves_layers_removed += 1

            for _ in range(size):
                node = q.popleft()

                for _next in graph[node]:
                    degrees[_next] -= 1
                    if degrees[_next] == 1:
                        q.append(_next)

        if remaining_nodes == 2:
            return 2 * leaves_layers_removed + 1

        return 2 * leaves_layers_removed