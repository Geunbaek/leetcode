class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        answer = float('inf')
        
        for num in nums:
            if num % 2 == 0:
                heappush(h, -num)
            else:
                heappush(h, -num * 2)
        
        _min = -max(h)
       
        while True:
            _max = -heappop(h)
            answer = min(answer, _max - _min)
    
            if _max % 2:
                break

            heappush(h, -_max // 2)
            _min = min(_min, _max // 2)

        return answer
            