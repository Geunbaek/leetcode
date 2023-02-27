"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def get_quad_tree(n, cur_x, cur_y):
            els = set()
            node = Node(0, 0, None, None, None, None)
            for y in range(cur_y, cur_y + n):
                for x in range(cur_x, cur_x + n):
                    els.add(grid[y][x])
            
            if len(els) == 1:
                node.isLeaf = 1
                node.val = els.pop()
                return node

            count = 0
            for y in range(cur_y, cur_y + n, n // 2):
                for x in range(cur_x, cur_x + n, n // 2):
                    child = get_quad_tree(n // 2, x, y)

                    if count == 0:
                        node.topLeft = child
                    elif count == 1:
                        node.topRight = child
                    elif count == 2:
                        node.bottomLeft = child
                    else:
                        node.bottomRight = child
                    count += 1
            return node
        
        return get_quad_tree(len(grid), 0, 0)
        