class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        _max = float('-inf')
        _min = float("inf")

        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num

            _min = min(_min, prefix_sum)
            _max = max(_max, prefix_sum)

            if prefix_sum >= 0:
                answer = max(
                    answer, 
                    max(prefix_sum, prefix_sum - _min)
                )
            else:
                answer = max(
                    answer,
                    max(abs(prefix_sum), abs(prefix_sum - _max))
                )
        return answer