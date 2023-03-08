class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) * h
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / mid)
            
            if time <= h:
                right = mid - 1
                answer = min(answer, mid)
            else:
                 left = mid + 1
                
        return answer