# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        counter = defaultdict(int)
        counter[root.val] += 1
        total = 1
        answer = 0
    
        def dfs(node):
            nonlocal answer, total
            if(not node.left and not node.right):
                oddCount = 0
                for count in counter.values():
                    if(total % 2 == 0):
                        if(count % 2 != 0):
                            return
                    else:
                        if(count % 2 != 0):
                            oddCount += 1
                            if(oddCount > 1):
                                return
                            
                answer += 1
        
            if(node.left):
                counter[node.left.val] += 1
                total += 1
                dfs(node.left)
                counter[node.left.val] -= 1
                total -= 1
            if(node.right):
                counter[node.right.val] += 1
                total += 1
                dfs(node.right)
                counter[node.right.val] -= 1
                total -= 1
        dfs(root)
        return answer