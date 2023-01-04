from collections import Counter
    
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        dp = [0 for _ in range(len(tasks) + 1)]
        if len(tasks) >= 2:
            dp[2] = 1
        if len(tasks) >= 3:
            dp[3] = 1
        
        for i in range(4, len(tasks) + 1):
            temp = []
            if dp[i - 2]:
                temp.append(dp[i - 2] + 1)
            if dp[i - 3]:
                temp.append(dp[i - 3] + 1)

            if temp:
                dp[i] = min(temp)
            else:
                dp[i] = 0

        answer = 0
        for num, cnt in counter.most_common():
            
            if not dp[cnt]:
                return -1
            answer += dp[cnt]
        return answer
        
        