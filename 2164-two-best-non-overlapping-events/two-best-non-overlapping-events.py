class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])

        h = []
        max_val = 0
        max_sum = 0
        for s, e, c in events:
            while h and h[0][0] < s:
                max_val = max(max_val, heapq.heappop(h)[-1])
            max_sum = max(max_sum, max_val + c)
            heapq.heappush(h, (e, c))
        return max_sum