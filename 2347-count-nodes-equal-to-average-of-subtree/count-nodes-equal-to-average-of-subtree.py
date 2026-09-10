# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dp(node):
            nodes = []
            target_node = 0
            if node.left:
                sub_node, cnt = dp(node.left)
                nodes.extend(sub_node)
                target_node += cnt
 
            if node.right:
                sub_node, cnt = dp(node.right)
                nodes.extend(sub_node)
                target_node += cnt

            nodes.append(node.val)
            if sum(nodes) // len(nodes) == node.val:
                target_node += 1
            return nodes, target_node
        return dp(root)[1]
