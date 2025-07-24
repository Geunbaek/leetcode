class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        h = [(0, 0)]
        visited = set()

        answer = float('inf')
        while h:
            cnt, now = heappop(h)

            if now == n - 1:
                answer = min(answer, cnt)
                continue

            for _next in range(now + 1, now + nums[now] + 1):
                if _next >= n:
                    continue

                if _next in visited:
                    continue

                visited.add(_next)
                heappush(h, (cnt + 1, _next))
        return answer
        