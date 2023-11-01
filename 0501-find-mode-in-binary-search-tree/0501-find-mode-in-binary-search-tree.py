# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        
        def dfs(node):
            if node:
                nodes.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        answer = []
        
        _max = -1
        for num, c in Counter(nodes).most_common():
            if _max == -1:
                _max = c
            if c == _max:
                answer.append(num)
        return answer