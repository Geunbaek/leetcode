class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
        n = len(nums)

        for i, num in enumerate(nums):
            heapq.heappush(h, (num, i))


        for _ in range(k):
            num, i = heapq.heappop(h)
            heapq.heappush(h, (num * multiplier, i))
        answer = [0 for _ in range(n)]

        while h:
            num, i = heapq.heappop(h)
            answer[i] = num

        return answer