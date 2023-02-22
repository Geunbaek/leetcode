class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2
            count = 1
            now = 0
            for w in weights:
                now += w
                if now > mid:
                    count += 1
                    now = w
                
            if count > days:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
    
    