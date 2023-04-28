class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        def check(a, b):
            diff = 0
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    diff += 1
            return diff <= 2 
        
        p = [i for i in range(len(strs))]
        
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if check(strs[i], strs[j]):
                    union(i, j)
              
        groups = set()
        for i in range(len(strs)):
            groups.add(find(i))
            
        return len(groups)
                
        