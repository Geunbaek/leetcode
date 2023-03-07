class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, 1_000_000_000_000_000
        
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for t in time:
                total += mid // t
       
            if total >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        