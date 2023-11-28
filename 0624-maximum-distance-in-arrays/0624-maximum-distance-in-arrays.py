class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        
        min_h, max_h = [], []
        
        for i in range(n):
            heapq.heappush(min_h, (arrays[i][0], i))
            heapq.heappush(max_h, (-arrays[i][-1], i))
            
        if len(min_h) == 1:
            _min1, _min2 = min_h[0], min_h[0]
            _max1, _max2 = max_h[0], max_h[0]
        else:
            _min1, _min2 = heapq.heappop(min_h), min_h[0]
            _max1, _max2 = heapq.heappop(max_h), max_h[0]
        
        if _min1[1] == _max1[1]:
            return max(-_max1[0] - _min2[0], -_max2[0] - _min1[0])
        return -_max1[0] - _min1[0]