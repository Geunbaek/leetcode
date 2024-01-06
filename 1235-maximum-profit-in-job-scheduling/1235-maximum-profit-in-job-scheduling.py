class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        
        h = []
        jobs = list(zip(startTime, endTime, profit))
        
        jobs.sort()
        _max = 0
        
        for s, e, p in jobs:

            while h and s >= h[0][0]:
                end, profit = heapq.heappop(h)
                _max = max(_max, profit)
                
            heapq.heappush(h, (e, p + _max))
            
        ans = 0
        
        while h:
            e, p = heapq.heappop(h)
            ans = max(ans, p)
        return ans
            
            
                
            
        