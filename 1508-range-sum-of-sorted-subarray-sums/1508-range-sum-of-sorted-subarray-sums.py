class Solution:
    def rangeSum(self, nums, n, left, right):
        h = []
        for i in range(n):
            heapq.heappush(h, (nums[i], i))

        ans = 0
        mod = 1_000_000_007
        for i in range(1, right + 1):
            _min = heapq.heappop(h)
            
            if i >= left:
                ans = (ans + _min[0]) % mod
                
            if _min[1] < n - 1:
                _min = (_min[0] + nums[_min[1] + 1], _min[1] + 1)
                heapq.heappush(h, _min)
        return int(ans)