

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.INF = 1_000_000_000
        self.graph = [[] for _ in range(n)]
        
        for u, v, c in edges:
            self.graph[u].append((v, c))
        

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.graph[u].append((v, c))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        h = []
        dist = [self.INF for _ in range(len(self.graph))]
        
        heapq.heappush(h, (0, node1))
        
        while h:
            cost, node = heapq.heappop(h)
            
            if dist[node] > cost:
                dist[node] = cost
                
                for _next, c in self.graph[node]:
                    if dist[_next] > cost + c:
                        heapq.heappush(h, (cost + c, _next))
        if dist[node2] == self.INF:
            return -1
        return dist[node2]
                
                
        
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)