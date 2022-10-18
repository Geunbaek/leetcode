from collections import deque

class Solution:
    def checkAnswer(self, answer):
        ret = []
        
        for char in answer:
            if not ret or ret[-1][0] != char:
                ret.append([char, 1])
            else:
                ret[-1][1] += 1
        answer = ""
        
        for char, count in ret:
            answer += f"{count}{char}"
        return answer
        
        
        
    def countAndSay(self, n: int) -> str:
        dp = ["" for _ in range(n)]
        dp[0] = '1'
        
        for i in range(1, n):
            dp[i] = self.checkAnswer(dp[i - 1])
            
        return dp[-1]