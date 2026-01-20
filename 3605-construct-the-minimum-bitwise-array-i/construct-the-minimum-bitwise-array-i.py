class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [-1 for _ in range(n)]

        for i in range(n):
            num = nums[i]
            for j in range(1, num):
                if j | j + 1 == num:
                    ans[i] = j
                    break
        return ans