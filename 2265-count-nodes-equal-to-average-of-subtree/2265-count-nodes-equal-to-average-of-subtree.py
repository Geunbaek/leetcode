# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def recur(node):
            nonlocal answer
            if node.left is None and node.right is None:
                answer += 1
                return node.val, 1

            ret = node.val
            total = 1
            if node.left:
                _sum, cnt = recur(node.left)
                ret += _sum
                total += cnt
            if node.right:
                _sum, cnt = recur(node.right)
                ret += _sum
                total += cnt
           
            if node.val == ret // total:
                answer += 1
            return ret, total 
        
        recur(root)
        return answer
        
            
        