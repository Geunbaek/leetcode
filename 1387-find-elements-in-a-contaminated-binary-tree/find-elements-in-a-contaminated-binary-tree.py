# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cache = set()
        self.recover(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.cache

    def recover(self, node, index):
        if node is None:
            return

        node.val = index
        self.cache.add(index)
        self.recover(node.left, 2 * index + 1)
        self.recover(node.right, 2 * index + 2)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)