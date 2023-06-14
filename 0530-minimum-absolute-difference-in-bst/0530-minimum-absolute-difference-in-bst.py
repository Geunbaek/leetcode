# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answers = []
        
        def dfs(node):
            answers.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        answers.sort()
        answer = float('inf')
        
        for u, v in zip(answers, answers[1:]):
            answer = min(answer, v - u)
        return answer
            
        