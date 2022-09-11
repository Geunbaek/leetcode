import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineerInfo = [[s, e] for s, e in zip(speed, efficiency)]
        engineerInfo.sort(key = lambda x: -x[-1])
        
        h = []
        _sum = 0
        answer = 0
        
        for s, e in engineerInfo:
            while len(h) > k - 1:
                _sum -= heapq.heappop(h)
            
            heapq.heappush(h, s)
            _sum += s
            
            answer = max(answer, _sum * e)
        return answer % (10 ** 9 + 7)
            