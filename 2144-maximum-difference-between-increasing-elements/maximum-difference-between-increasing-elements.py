class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        stack = []
        answer = -1
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()

            stack.append(num)
            if len(stack) >= 2:
                answer = max(answer, stack[-1] - stack[0])
        return answer