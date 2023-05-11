class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [
            [0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)
        ]
        
        for y in range(1, len(nums1) + 1):
            for x in range(1, len(nums2) + 1):
                num1, num2 = nums1[y - 1], nums2[x - 1]
                if num1 == num2:
                    dp[y][x] = dp[y - 1][x - 1] + 1
                else:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
                    
        return dp[-1][-1]
        