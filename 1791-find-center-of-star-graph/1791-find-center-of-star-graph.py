class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            
        for node, count in degree.items():
            if count == len(degree) - 1:
                return node
        return -1