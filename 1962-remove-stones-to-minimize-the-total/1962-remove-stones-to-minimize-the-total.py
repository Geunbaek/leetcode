import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h=[-pile for pile in piles]
        heapq.heapify(h)
        
        for _ in range(k):
            _max=-heapq.heappop(h)
            
            heapq.heappush(h,-(_max-math.floor(_max/2)))
        return -sum(h)
        
        