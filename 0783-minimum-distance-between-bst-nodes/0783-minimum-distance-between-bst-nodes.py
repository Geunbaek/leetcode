# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            nodes.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
                
        nodes = []
        dfs(root)
        answer = float('inf')
        nodes.sort()
        for i in range(1, len(nodes)):
            answer = min(answer, nodes[i] - nodes[i - 1])
        return answer
        