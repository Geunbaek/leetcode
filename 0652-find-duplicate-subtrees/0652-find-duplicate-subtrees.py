# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            if node is None:
                return ""
            
            r = f"({dfs(node.left)})" + str(node.val) + f"({dfs(node.right)})"
            cache[r] += 1
            if cache[r] == 2:
                answer.append(node)
            return r
            
        cache = defaultdict(int)
        answer = []
        dfs(root)
        return answer
        