# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MAX = 50_001
        MOD = 1_000_000_007
        memo = defaultdict(int)

        def dfs(node, index):
            if not node: return 0
            _sum = node.val
            _sum += dfs(node.left, index * 2)
            _sum += dfs(node.right, index * 2 + 1)
            memo[index] = _sum
            return _sum

        total = dfs(root, 1)
        maxProduct = 0
        for i, value in memo.items():
            maxProduct = max(maxProduct, (value * (total - value)))

        return maxProduct % MOD