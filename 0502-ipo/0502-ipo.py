import heapq
from collections import deque

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = deque(sorted(list(zip(capital, profits))))
        
        h = []
    
        for i in range(k):
            while arr and arr[0][0] <= w:
                heapq.heappush(h, -arr.popleft()[1])
                
            if not h:
                break
            w += -heapq.heappop(h)
        return w