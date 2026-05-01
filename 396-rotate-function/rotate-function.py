class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = sum(nums)

        now = sum([i * num for i, num in enumerate(nums)])
        print(now)
        ans = now

        for i in range(n - 1, 0, -1):
            now = now + _sum - n * nums[i]
            ans = max(ans, now)
            
        return ans