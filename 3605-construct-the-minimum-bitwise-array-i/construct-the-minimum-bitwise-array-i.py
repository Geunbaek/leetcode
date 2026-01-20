class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [-1 for _ in range(n)]

        for i in range(n):
            if not nums[i] % 2:
                continue

            ans[i] = nums[i] - ((nums[i] + 1) & (-nums[i] - 1)) // 2
        return ans