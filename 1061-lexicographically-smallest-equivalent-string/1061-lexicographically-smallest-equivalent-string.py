class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            if ap < bp:
                p[bp] = ap
            else:
                p[ap] = bp
        
        p = [i for i in range(26)]
        
        for c1, c2 in zip(s1, s2):
            c1 = ord(c1) - ord('a')
            c2 = ord(c2) - ord('a')
            if find(c1) != find(c2):
                union(c1,c2)
            
        answer = []
        for char in baseStr:
            c = ord(char) - ord('a')
            answer.append(chr(find(c) + ord('a')))
            
        return "".join(answer)
        