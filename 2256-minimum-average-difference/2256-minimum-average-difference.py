class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        min_diff = float('inf')
        N = len(nums)
        answer = 0
        
        for i, num in enumerate(nums):
            m = i + 1
            
            left_sum += num
            right_sum -= num
            
            if i != N - 1:
                avg_diff = abs((left_sum // m) - (right_sum // (N - m)))
            else:
                avg_diff = abs((left_sum // m) - 0)

            if min_diff > avg_diff:
                answer = i
                min_diff = avg_diff
                
        return answer
            