# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        cache = {}
        degree = defaultdict(int)
        
        for root, child, isLeft in descriptions:
            node = cache.get(root, TreeNode(root))
            cache[root] = node
            if isLeft == 1:
                left_node = cache.get(child, TreeNode(child))
                node.left = left_node
                cache[child] = left_node
            else:
                right_node = cache.get(child, TreeNode(child))
                node.right = right_node
                cache[child] = right_node
            degree[child] += 1

        for root, _, _ in descriptions:
            if root not in degree:
                return cache[root]
        return -1
        