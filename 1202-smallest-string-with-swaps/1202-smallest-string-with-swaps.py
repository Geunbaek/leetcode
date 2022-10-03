from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
        
        p = [i for i in range(len(s))]
        
        for a, b in pairs:
            if find(a) != find(b):
                union(a, b)
                
        
        pDic = defaultdict(list)
        
        for i in range(len(s)):
            pDic[find(i)].append(s[i])
        
        for key, val in pDic.items():
            val.sort(reverse=True)
        
        answer = ""
        
        for i in range(len(s)):
            answer += pDic[find(i)].pop()
            
        return answer
        