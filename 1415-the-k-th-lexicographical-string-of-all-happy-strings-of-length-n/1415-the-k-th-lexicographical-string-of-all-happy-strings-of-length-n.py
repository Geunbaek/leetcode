class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        answer = []
        def dfs(depth, path):
            if depth >= n:
                answer.append(path)
                return
            for i in ('a', 'b', 'c'):
                if path[-1] != i:
                    dfs(depth + 1, path + i)
        
        for i in ("a", 'b', 'c'):
            dfs(1, i)
            
        if len(answer) >= k:
            return answer[k - 1]
        return ""

        
                
                  
        
            
        