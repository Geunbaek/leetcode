class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = nums
        heapify(h)
        answer = 0
        while h and len(h) >= 2:
            x = heappop(h)
            y = heappop(h)
            if (x >= k):
                heappush(h, x)
                heappush(h, y)
                break

            heappush(h, min(x, y) * 2 + max(x, y))
            answer += 1
        return answer