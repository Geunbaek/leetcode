class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        h = [(0, 0)]
        visited = set([0])

        while h:
            now, cnt = heappop(h)
            now = -now

            if now == n - 1:
                return True

            for i in range(1, nums[now] + 1):
                _next = now + i
                if _next >= n:
                    continue
                if _next in visited:
                    continue 
                visited.add(_next)
                heappush(h, (-_next, cnt + 1))
        return False

            


