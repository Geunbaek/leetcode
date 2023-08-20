from collections import deque, defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_count = m
        
        for i in range(n):
            if group[i] == -1:
                group[i] = group_count
                group_count += 1

        
        degree = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        q = deque()
        visited = []
        
        group_degree = [0 for _ in range(group_count)]
        group_graph = [[] for _ in range(group_count)]
        group_q = deque()
        group_visited = []
        
        for i, beforeItem in enumerate(beforeItems):
            for item in beforeItem:
                graph[item].append(i)
                degree[i] += 1
                if group[i] != group[item]:
                    group_graph[group[item]].append(group[i])
                    group_degree[group[i]] += 1
                    
        
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
                
        for i in range(group_count):
            if group_degree[i] == 0:
                group_q.append(i)
                
        while q:
            now = q.popleft()
            visited.append(now)
            for _next in graph[now]:
                degree[_next] -= 1
                if degree[_next] == 0:
                    q.append(_next)
    
        while group_q:
            now = group_q.popleft()
            group_visited.append(now)
            for _next in group_graph[now]:
                group_degree[_next] -= 1
                if group_degree[_next] == 0:
                    group_q.append(_next)
                
        if len(visited) != n or len(group_visited) != group_count:
            return []
        
        ordered_groups = defaultdict(list)
        
        for item in visited:
            ordered_groups[group[item]].append(item)
 
        answer = []
        
        for i in group_visited:
            answer.extend(ordered_groups[i])
        return answer
        
                
                
                
        
        
        