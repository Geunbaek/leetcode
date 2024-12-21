class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        answer = 0

        visited = set()
        
        def dfs(node):
            nonlocal answer
            is_leaf = True
            ret = values[node]
            for _next in tree[node]:
                if _next in visited:
                    continue
                visited.add(_next)
                is_leaf = False
                ret += dfs(_next)

            if ret % k == 0:
                answer += 1
                return 0

            return ret

        tree = [[] for _ in range(n)]

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        visited.add(0)
        dfs(0)
        return answer
        

        
        