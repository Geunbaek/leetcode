class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        def dfs(depth, path):
            if depth <= 0:
                if len(path) == 4:
                    answer.append(".".join(path[::-1]))
         
            for i in range(depth - 1, -1, -1):
                if s[depth: i + 1] == "0":
                    continue
                if int(s[i: depth]) >= 256:
                    continue
                if str(int(s[i: depth])) != s[i: depth]:
                    continue
                dfs(i, path + [s[i: depth]])
                
        dfs(len(s), [])
        return answer
        