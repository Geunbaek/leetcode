"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        def bfs(start_node):
            visited = dict()
            q = deque([start_node])
            visited[start_node.val] = Node(start_node.val, start_node.neighbors)
            
            while q:
                cur = q.popleft()
                for _next in cur.neighbors:
                    if _next.val in visited:
                        continue
                    visited[_next.val] = Node(_next.val, _next.neighbors)
                    q.append(_next)
            
            for key, val in visited.items():
                new_ne = []
                for _next in visited[key].neighbors:
                    new_ne.append(visited[_next.val])
                visited[key].neighbors = new_ne
            return visited[start_node.val]
        
        return bfs(node)
            
