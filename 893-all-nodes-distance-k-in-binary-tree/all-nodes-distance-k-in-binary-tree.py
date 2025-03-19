# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def recur(parent, node):        
            if parent:
                graph[node.val].append(parent.val)
            
            if node.left:
                graph[node.val].append(node.left.val)
                recur(node, node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                recur(node, node.right)
        
        recur(None, root)
        
        q = deque([(target.val, 0)])
        visited = set([target.val])
        answer = []

        while q:
            now, dist = q.popleft()
            
            if dist == k:
                answer.append(now)
                continue

            for _next in graph[now]:
                if _next in visited:
                    continue
                visited.add(_next)
                q.append((_next, dist + 1))
        return answer