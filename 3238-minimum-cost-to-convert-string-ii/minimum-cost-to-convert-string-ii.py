from collections import defaultdict
from typing import List
import heapq


class TrieNode:
    def __init__(self):
        self.children = {}
        self.id = -1 

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        idx_map = {}
        counter = 0
        
        def get_id(s):
            nonlocal counter
            if s not in idx_map:
                idx_map[s] = counter
                counter += 1
            return idx_map[s]
        
        inf = float('inf')
        for o, c in zip(original, changed):
            get_id(o)
            get_id(c)
            
        num_nodes = counter
        dist = [[inf] * num_nodes for _ in range(num_nodes)]
        
        for i in range(num_nodes):
            dist[i][i] = 0
            
        for o, c, w in zip(original, changed, cost):
            u, v = get_id(o), get_id(c)
            dist[u][v] = min(dist[u][v], w)
            
        for k in range(num_nodes):
            for i in range(num_nodes):
                if dist[i][k] == inf: continue
                for j in range(num_nodes):
                    if dist[k][j] == inf: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        root = TrieNode()
        for s in original:
            node = root
            for char in s:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.id = idx_map[s] 

        n = len(source)
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == inf:
                continue
            
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            node = root
            for j in range(i, n):
                char = source[j]
                if char not in node.children:
                    break
                node = node.children[char]
                
                if node.id != -1:
                    src_id = node.id
                    target_sub = target[i : j+1]
                    if target_sub in idx_map:
                        dst_id = idx_map[target_sub]
                        if dist[src_id][dst_id] != inf:
                            dp[j+1] = min(dp[j+1], dp[i] + dist[src_id][dst_id])
                            
        result = dp[n]
        return result if result != inf else -1