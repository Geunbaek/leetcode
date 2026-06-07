# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        p = defaultdict(int)
        cache = {}

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        for parent, child, is_left in descriptions:
            if parent not in cache:
                cache[parent] = TreeNode(parent)
                p[parent] = parent
            if child not in cache:
                cache[child] = TreeNode(child)
                p[child] = child
            if is_left:
                cache[parent].left = cache[child]
            else:
                cache[parent].right = cache[child]
            
            union(child, parent)
        root = find(descriptions[0][0])

        return cache[root]


