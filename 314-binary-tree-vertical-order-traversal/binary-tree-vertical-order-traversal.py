# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, vertical_index, depth):
            if not node:
                return

            if vertical_index not in vertical_index_set:
                vertical_index_set.add(vertical_index)

            dfs(node.left, vertical_index - 1, depth + 1)
            cache[vertical_index].append({
                "val": node.val,
                "depth": depth
            })
            dfs(node.right, vertical_index + 1, depth + 1)
            
        cache = defaultdict(list)
        vertical_index_set = set()

        dfs(root, 0, 0)

        answer = []

        for v_index in sorted(vertical_index_set):
            answer.append(
                list(
                    map(
                        lambda x: x["val"],
                        sorted(cache[v_index], key = lambda x: x["depth"])
                    )
                )
            )

        return answer

        