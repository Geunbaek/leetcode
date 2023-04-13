class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and popped and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
        if popped:
            return False
        return True
            