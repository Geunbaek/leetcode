# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def get_depth(start, depth):
            high = ""
            for i in range(start, n):
                if traversal[i] != "-":
                    break
                high += traversal[i]
            return high

        def split(depth, left, right):
            ret = []
            i = left
            while (i <= right):
                if traversal[i] != "-":
                    i += 1
                    continue
                high = get_depth(i, depth)
                if len(high) == depth:
                    if ret:
                        ret[-1].append(i - 1)
                    ret.append([])
                    ret[-1].append(i + depth)
                i += len(high) + 1
            ret[-1].append(right)
            return ret

        def get_root_value(left, right):
            value = ""

            for i in range(left, right + 1):
                if traversal[i].isdigit():
                    value += traversal[i]
                else:
                    break

            return value
        
        def divide(depth, left, right):
            if left > right:
                return None
        
            root_value = get_root_value(left, right)
            root = TreeNode(int(root_value))
            
            if left + len(root_value) >= right:
                return root

            starts = split(depth, left + len(root_value), right)
            
            if len(starts) >= 1:
                root.left = divide(depth + 1, starts[0][0], starts[0][1])
            
            if len(starts) >= 2:
                root.right = divide(depth + 1, starts[1][0], starts[1][1])

            return root


        n = len(traversal)
        root = divide(1, 0, n - 1)
        return root




