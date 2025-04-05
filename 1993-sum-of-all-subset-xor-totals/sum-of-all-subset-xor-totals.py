class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer |= num
        return answer << (len(nums) - 1)