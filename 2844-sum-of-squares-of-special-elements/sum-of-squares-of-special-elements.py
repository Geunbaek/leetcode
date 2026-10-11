class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(map(lambda x: x[1] * x[1], filter(lambda x: len(nums) % (x[0] + 1) == 0, enumerate(nums))))