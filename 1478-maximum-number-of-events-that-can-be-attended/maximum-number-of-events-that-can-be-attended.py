class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        max_days = max(events, key = lambda x: x[1])[1]
        events = deque(events)
        h = []
        dp = [0 for _ in range(100_001)]

        for i in range(1, max_days + 1):
            while events and events[0][0] <= i <= events[0][1]:
                start, end = events.popleft()
                heappush(h, end)
            
            while h and h[0] < i:
                heappop(h)

            if h:
                heappop(h)
                dp[i] += 1
        return sum(dp)

