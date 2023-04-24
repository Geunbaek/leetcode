import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
       
        while len(h) > 1:
            first = -heapq.heappop(h)
            second = -heapq.heappop(h)
            if first == second:
                continue
            heapq.heappush(h, -abs(first - second))
        if not h:
            return 0
        return -heapq.heappop(h)

        