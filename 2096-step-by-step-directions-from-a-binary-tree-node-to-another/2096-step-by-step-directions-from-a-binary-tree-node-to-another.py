# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def recur(parent, node):                
            cache[node.val] = { "node": node, "parent": parent }
            if node.left:
                recur(node, node.left)
            if node.right:
                recur(node, node.right)
        
        def bfs():
            q = deque()
            q.append((cache[startValue], ""))
            
            visited = set()
            visited.add(startValue)
            while q:
                
                nodeInfo, oper = q.popleft()
                node = nodeInfo["node"]
                parent = nodeInfo["parent"]
                if node.val == destValue:
                    return oper
                if parent:
                    if parent.val not in visited:
                        visited.add(parent.val)
                        q.append((cache[parent.val], oper + "U"))
                if node.left:
                    if node.left.val not in visited:
                        visited.add(node.left.val)
                        q.append((cache[node.left.val], oper + "L"))
                if node.right:
                    if node.right.val not in visited:
                        visited.add(node.right.val)
                        q.append((cache[node.right.val], oper + "R"))
            return ""
                
        cache = dict()
        recur(None, root)
        return bfs()
        
        
            