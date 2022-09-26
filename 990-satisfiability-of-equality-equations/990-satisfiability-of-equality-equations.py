
class Solution:
    
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
    
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        equations.sort(key = lambda x: x[1:-1], reverse=True)
        p = [i for i in range(26)]
        
        for equation in equations:
            a, equalSign, b = re.split(r"([=|!]=)", equation)
            if equalSign == "==":
                union(ord(a) - ord('a'),(ord(b) - ord('a')))
            else:
                if find(ord(a) - ord('a')) == find(ord(b) - ord('a')):
                    return False
    
        return True
        