class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        h = []
        
        for d, s in zip(dist, speed):
            heapq.heappush(h, (d / s))
        
        day = 0
        answer = 0
        while h:
            if h[0] > day:
                heapq.heappop(h)
                answer += 1
            else:
                break

            day += 1
        return answer
                
                
                
            
        