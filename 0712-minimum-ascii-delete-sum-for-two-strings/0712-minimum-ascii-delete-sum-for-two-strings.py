class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = " " + s1
        s2 = " " + s2
        
        dp = [[[0, set(), 0] for _ in range(len(s1))] for _ in range(len(s2))]
        
        for y in range(1, len(s2)):
            for x in range(1, len(s1)):
                if s1[x] == s2[y]:
                    dp[y][x][0] = dp[y - 1][x - 1][0] + 1
                    dp[y][x][1] = dp[y - 1][x - 1][1] | {(x, y)}
                    dp[y][x][2] = dp[y - 1][x - 1][2] + ord(s1[x])
                else:
                    if dp[y-1][x][2] > dp[y][x-1][2]:
                        dp[y][x] = dp[y - 1][x]
                    else:
                        dp[y][x] = dp[y][x - 1]
    

        result = dp[-1][-1][1]
        answer = 0
        visited = [[0 for _ in range(len(s1))], [0 for _ in range(len(s2))]]
        
        for x, y in result:
            visited[0][x] += 1
            visited[1][y] += 1
            
        for x in range(1, len(s1)):
            if visited[0][x] == 0:
                answer += ord(s1[x])
                
        for y in range(1, len(s2)):
            if visited[1][y] == 0:
                answer += ord(s2[y])
                
        
        return answer
        