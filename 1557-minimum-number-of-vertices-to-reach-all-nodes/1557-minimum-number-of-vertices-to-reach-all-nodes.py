class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0 for _ in range(n)]
        
        for u, v in edges:
            degree[v] += 1
            
        answer = []
        
        for i, count in enumerate(degree):
            if count == 0:
                answer.append(i)
        return answer
            