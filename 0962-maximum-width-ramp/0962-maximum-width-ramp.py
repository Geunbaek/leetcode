class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        
        for i, num in enumerate(nums):
            if not stack or stack[-1][1] > num:
                stack.append((i, num))
      
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1][1] <= nums[i]:
                j, _ = stack.pop()
                answer = max(answer, i - j)
        return answer
        
        