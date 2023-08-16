import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        h = []
        
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))

        answer = []
        
        while right < len(nums):
            _max, index = h[0]
            
            while index < left:
                heapq.heappop(h)
                _max, index = h[0]
                
            answer.append(-_max)
            left += 1
            right += 1
            if right >= len(nums):
                break
            heapq.heappush(h, (-nums[right], right))
        return answer
            
            