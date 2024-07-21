class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topology_sort(condition):
            graph = [[] for _ in range(k + 1)]
            degrees = [0 for _ in range(k + 1)]
            order = []
            
            for u, v in condition:
                graph[u].append(v)
                degrees[v] += 1
                
            q = deque()
            
            for i, degree in enumerate(degrees):
                if degree == 0:
                    q.append(i)
                    
            while q:
                now = q.popleft()
                order.append(now)
                
                for _next in graph[now]:
                    degrees[_next] -= 1
                    if degrees[_next] == 0:
                        q.append(_next)
                        
            return order[1:]
        
        row_order = topology_sort(rowConditions)
        col_order = topology_sort(colConditions)

        
        if len(row_order) < k or len(col_order) < k:
            return []
        
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        for y in range(k):
            for x in range(k):
                if row_order[y] == col_order[x]:
                    matrix[y][x] = row_order[y]
        return matrix
     
            
            
        