class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = []
        h = []
        for d, p in zip(difficulty, profit):
            heapq.heappush(jobs, (d, p))
            
        worker.sort()
        answer = 0
        for ability in worker:
            while jobs and jobs[0][0] <= ability:
                d, p = heapq.heappop(jobs)
                heapq.heappush(h, -p)
            if h:
                answer += -h[0]
        return answer