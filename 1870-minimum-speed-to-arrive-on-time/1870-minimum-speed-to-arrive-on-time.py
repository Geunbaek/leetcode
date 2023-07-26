class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 1, 10_000_000_000
        answer = 10_000_000_001
        
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for i, d in enumerate(dist):
                if i == len(dist) - 1:
                    time += d / mid
                    continue
                time += math.ceil(d / mid)
     
            if time <= hour:
                right = mid - 1
                answer = min(answer, mid)
            elif time > hour:
                left = mid + 1
        if answer == 10_000_000_001:
            return -1
        return answer
                