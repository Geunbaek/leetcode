from collections import deque

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        def dfs(path, depth):

            if depth == 0:
                return 1
            
            if (path, depth) in cache:
                return cache[(path, depth)] % MOD
            
            ret = 0
            for _next in graph[path[-1]]:
                ret += dfs(_next, depth - 1)
            cache[(path, depth)] = ret % MOD
            return cache[(path, depth)] % MOD

        MOD = 10**9 + 7
        graph = {
            "s": ["a", "e", "i", "o", "u"],
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        cache = dict()
     
        return dfs("s", n) % MOD
        
        