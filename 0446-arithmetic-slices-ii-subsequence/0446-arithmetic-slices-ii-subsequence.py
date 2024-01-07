class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        
        for y in range(n):
            for x in range(y):
                diff = nums[y] - nums[x]
                ans += dp[x][diff]
                # print(dp[x][diff])
                dp[y][diff] += dp[x][diff] + 1
        # for l in dp:
        #     print(l)
        return ans
        
        