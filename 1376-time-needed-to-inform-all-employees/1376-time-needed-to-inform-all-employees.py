from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        
        for i, head in enumerate(manager):
            if head == -1:
                continue
            graph[head].append(i)
            
        
        q = deque([(headID, informTime[headID])])
        answer = 0
        
        while q:
            now, time = q.popleft()
            answer = max(answer, time)
            for _next in graph[now]:
                q.append((_next, time + informTime[_next]))
            
        
        return answer