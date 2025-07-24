
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        answer = float("inf")

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        total = 0
        for num in nums:
            total ^= num

        def calc(p1, p2, p3):
            return max(p1, p2, p3) - min(p1, p2, p3)
        
        def dfs(node, parent):
            children = nums[node]

            for _next in graph[node]:
                if _next == parent:
                    continue
                
                children ^= dfs(_next, node)
            
            for _next in graph[node]:
                if _next != parent:
                    continue
                
                dfs2(_next, node, children, node)
            return children

        def dfs2(node, parent, others, ancestor):
            nonlocal answer
            children = nums[node]

            for _next in graph[node]:
                if _next == parent:
                    continue

                children ^= dfs2(_next, node, others, ancestor)

            if parent == ancestor:
                return children
            
            answer = min(answer, calc(others, children, total ^ others ^ children))
            return children
        dfs(0, -1)
        return answer
        