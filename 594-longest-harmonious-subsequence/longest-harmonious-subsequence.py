class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        r = 0
        answer = 0

        for l in range(n):
            while r < n - 1 and nums[r + 1] - nums[l] <= 1:
                r += 1
            
            if nums[r] - nums[l] == 1:
                answer = max(answer, r - l + 1)

        return answer