# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            head = TreeNode(val, root)
            return head
        def dfs(node, curDepth):
            if curDepth == depth - 1:
                if node.left:
                    node.left = TreeNode(val, node.left)
                else:
                    node.left = TreeNode(val)
                if node.right:
                    node.right = TreeNode(val, None, node.right)
                else:
                    node.right = TreeNode(val)
                return
            
            if node.left:
                dfs(node.left, curDepth + 1)
            if node.right:
                dfs(node.right, curDepth + 1)
                
        dfs(root, 1)
        return root