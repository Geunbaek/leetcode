# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def is_target_leaf_node(node):
            if node.left:
                if is_target_leaf_node(node.left):
                    node.left = None
            if node.right:
                if is_target_leaf_node(node.right):
                    node.right = None
            return node.left is None and node.right is None and node.val == target
        is_target_leaf_node(root)
        
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
        
        

            