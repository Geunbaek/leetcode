class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = []
        answer = [0 for _ in range(len(arr))]
        for i, score in enumerate(arr):
            heapq.heappush(ranks, (score, i))

        now = 1
        prev_score = -1_000_000_001
        while ranks:
            s, i = heapq.heappop(ranks)
            if s > prev_score:
                answer[i] = now
                now += 1
                prev_score = s
            else:
                answer[i] = now - 1
        return answer