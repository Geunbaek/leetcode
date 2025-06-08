class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        _max = float('-inf')
        for num in preorder:
            while stack and stack[-1] < num:
                _max = max(_max, stack.pop())

            if _max >= num:
                return False
            stack.append(num)
        return True

        