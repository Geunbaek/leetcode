import heapq
from collections import deque

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = deque()
        
        for i, cost in enumerate(costs):
            q.append((cost, i))
            
        left = []
        right = []
        h = []
        answer =0
        
        for _ in range(candidates):
            if q:
                heapq.heappush(left, q.popleft())
            if q:
                heapq.heappush(right, q.pop())
            
        for _ in range(k):
            if len(left) < candidates or len(right) < candidates:
                if not h:
                    h = left + right
                    heapq.heapify(h)
            
            if h:
                cost, i = heapq.heappop(h)
                answer += cost
            else:
                lf = heapq.heappop(left)
                rf = heapq.heappop(right)
                if lf[0] < rf[0]:
                    answer += lf[0]
                    heapq.heappush(right, rf)
                    if q:
                        heapq.heappush(left, q.popleft())
                elif lf[0] > rf[0]:
                    answer += rf[0]
                    heapq.heappush(left, lf)
                    if q:
                        heapq.heappush(right, q.pop())
                else:
                    answer += lf[0]
                    heapq.heappush(right, rf)
                    if q:
                        heapq.heappush(left, q.popleft())
                
        return answer
            