class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r = 1, maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2
        eps = 1e-7
        while l <= r:
            time = (l + r) // 2
            heights = 0
            
            for workerTime in workerTimes:
                work = time // workerTime
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                heights += k
            
            if heights < mountainHeight:
                l = time + 1
            else:
                r = time - 1
        return l