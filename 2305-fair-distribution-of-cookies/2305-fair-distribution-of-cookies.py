class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        costs = [0 for _ in range(k + 1)]
        answer = float("inf")
        

        def dfs(depth, count):
            nonlocal answer
            if n - depth < count:
                return
            
            if depth >= n:
                answer = min(answer, max(costs))
                return
            
            
            for j in range(1 , k + 1):
                if costs[j] == 0:
                    costs[j] += cookies[depth]
                    dfs(depth + 1, count - 1)
                    costs[j] -= cookies[depth]
                else:
                    costs[j] += cookies[depth]
                    dfs(depth + 1, count)
                    costs[j] -= cookies[depth]
                
        dfs(0, k)
        
        return answer
                    
                
                
        