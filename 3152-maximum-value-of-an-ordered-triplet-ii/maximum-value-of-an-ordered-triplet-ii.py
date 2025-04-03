class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        max_diff = 0
        max_value = 0

        for num in nums:
            answer = max(answer, max_diff * num)
            max_diff = max(max_diff, max_value - num)
            max_value = max(max_value, num)

        return answer