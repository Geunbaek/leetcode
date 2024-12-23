# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        nodes = []

        def compare_arr(arr1, arr2):
            count = 0
            n = len(arr1)

            numMap = dict()

            for i, num in enumerate(arr1):
                numMap[num] = i

            for i in range(n):
                if arr1[i] != arr2[i]:
                    num1 = arr1[i]
                    num2 = arr2[i]
                    arr1[i], arr1[numMap[num2]] = arr1[numMap[num2]], arr1[i]
                    numMap[num1] = numMap[num2]
                    numMap[num2] = i
                    count += 1
            return count


        def dfs(node, depth):
            if not node:
                return

            if len(nodes) <= depth:
                nodes.append([])

            nodes[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        answer = 0

        for node in nodes:
            sorted_node = sorted(node)
            diff = compare_arr(node, sorted_node)
            print(node, sorted_node, diff)
            answer += diff

        return answer
        