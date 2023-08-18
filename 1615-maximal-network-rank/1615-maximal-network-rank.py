class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connect = [[0 for _ in range(n)] for _ in range(n)]
        degree = [0 for _ in range(n)]
        
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            connect[u][v] = 1
            connect[v][u] = 1
            
        answer = 0            
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if connect[i][j] == 1:
                    answer = max(answer, degree[i] + degree[j] - 1)
                else:
                    answer = max(answer, degree[i] + degree[j])
        return answer
        