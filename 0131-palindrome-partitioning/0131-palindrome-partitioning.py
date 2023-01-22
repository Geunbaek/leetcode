class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palin(s):
            return s == s[::-1]
        answers = []
        def dfs(depth, ans):
            if depth == len(s):
                answers.append(ans)
                return 
                
            for i in range(depth, len(s)):
                word = s[depth: i + 1]
                if is_palin(word):
                    dfs(i + 1, ans + [word])
                    
        dfs(0, [])
        return answers