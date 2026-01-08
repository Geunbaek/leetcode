class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        c, r = len(nums1), len(nums2)
        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        for y in range(1, r + 1):
            num2 = nums2[y - 1]
            for x in range(1, c + 1):
                num1 = nums1[x - 1]
                prev_max = dp[y - 1][x - 1] 
                prev_y = dp[y - 1][x] if y - 1 != 0 else -float('inf')
                prev_x = dp[y][x - 1] if x - 1 != 0 else -float('inf')
                dp[y][x] = max(
                    num1 * num2,
                    prev_max + (num1 * num2),
                    prev_y,
                    prev_x
                )
    
        return dp[r][c]