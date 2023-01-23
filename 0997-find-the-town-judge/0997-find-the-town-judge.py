class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_degree = [0 for _ in range(n + 1)]
        trust_degree = [0 for _ in range(n + 1)]
        
        for u, v in trust:
            trusted_degree[v] += 1
            trust_degree[u] += 1
        
        for index, info in enumerate(zip(trusted_degree, trust_degree)):
            if index == 0:
                continue
            trusted, trust = info
            if trusted == n - 1 and trust == 0:
                return index 

        return -1
        
        