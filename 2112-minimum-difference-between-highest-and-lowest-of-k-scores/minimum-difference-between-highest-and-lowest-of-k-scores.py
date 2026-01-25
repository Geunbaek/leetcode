class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        n = len(nums)

        if n == 1:
            return 0

        nums.sort()
        answer = float('inf')
        for i in range(k - 1, n):
            answer = min(answer, nums[i] - nums[i - k + 1])
        return answer