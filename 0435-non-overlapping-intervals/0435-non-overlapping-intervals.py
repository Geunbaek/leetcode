import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[-1]))
        time = -float(inf)
        answer = 0
        
        for u, v in intervals:
            if u >= time:
                time = v
            else:
                answer += 1
                
        return answer