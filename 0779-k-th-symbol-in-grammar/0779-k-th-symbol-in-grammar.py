class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(depth, i, cur):
            if depth == 1:
                return cur
            
            total = 2 ** (depth - 1)
            
            if i > total / 2:
                return dfs(depth - 1, i - total / 2, 1 if cur == 0 else 0)
            else:
                return dfs(depth - 1, i, 0 if cur == 0 else 1)
            
            
        return  dfs(n, k, 0)   
       
    
                
                