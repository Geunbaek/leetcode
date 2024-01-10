# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def make_graph(node, parent):
            if not node:
                return
            
            if parent != 0:
                graph[parent].append(node.val)
                graph[node.val].append(parent)
                
            make_graph(node.left, node.val)
            make_graph(node.right, node.val)
            
        def dfs(node, depth):
            nonlocal ans
            ans = max(ans, depth)
            print(node, depth)
            for _next in graph[node]:
                if visited[_next] == 1:
                    continue
                visited[_next] = 1
                dfs(_next, depth + 1)
                
            
        
        graph = [[] for _ in range(100001)]
        visited = [0 for _ in range(100001)]
        ans = 0
        make_graph(root, 0)
        visited[start] = 1
        dfs(start, 0)
        return ans

        
        
        
        