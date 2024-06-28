class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0 for _ in range(n)]
        
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        point = [0 for _ in range(n)]
        
        rank = sorted(enumerate(degree), key = lambda x: x[-1])
        for i in range(n):
            node, cnt = rank[i]
            point[node] = i + 1
            
        answer = 0
        for u, v in roads:
            answer += point[u] + point[v]
            
        return answer
