class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = 0

        for num1, num2 in zip(nums, nums[1:] + [nums[0]]):
            answer = max(answer, abs(num1 - num2))
        return answer