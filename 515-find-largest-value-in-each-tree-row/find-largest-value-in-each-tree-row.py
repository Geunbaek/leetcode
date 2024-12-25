# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            nonlocal answer
            if not node:
                return

            if len(answer) <= depth:
                answer.append(float("-inf"))

            answer[depth] = max(answer[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        answer = []
        dfs(root, 0)
        return answer

        