class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        n = len(nums)
        for i in range(n // 2):
            answer = max(answer, nums[n - i - 1] + nums[i])

        return answer