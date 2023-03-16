from collections import deque

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        incre = [0]
        decre = deque([0])
        
        for i in range(1, n):
            if security[i] >= security[i - 1]:
                incre.append(incre[-1] + 1)
            else:
                incre.append(0)
                
        for i in range(n - 2, -1, -1):
            if security[i] >= security[i + 1]:
                decre.appendleft(decre[0] + 1)
            else:
                decre.appendleft(0)
        print(incre, decre)
        answer = []
        for i in range(time, n - time):
            if decre[i - time] - decre[i] >= time and incre[i + time] - incre[i] >= time:
                answer.append(i)
        return answer
                