# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []  

        def dfs(node, depth):
            if not node:
                return

            if len(nodes) <= depth:
                nodes.append([])

            nodes[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        def reverse_odd_node():
            ret = []
            for i in range(len(nodes)):
                if i % 2 != 0:
                    ret.extend(nodes[i][::-1])
                else:
                    ret.extend(nodes[i])
            return ret

        def make_binary_tree(parent, i, nodes):
            left = 2 * i + 1
            right = left + 1
            if left >= len(nodes):
                return

            left_node = TreeNode(nodes[left])
            right_node = TreeNode(nodes[right])

            parent.left = left_node
            parent.right = right_node
            make_binary_tree(left_node, left, nodes)
            make_binary_tree(right_node, right, nodes)

        dfs(root, 0)

        reversedNodes = reverse_odd_node()
        root = TreeNode(reversedNodes[0])

        make_binary_tree(root, 0, reversedNodes)
        return root



