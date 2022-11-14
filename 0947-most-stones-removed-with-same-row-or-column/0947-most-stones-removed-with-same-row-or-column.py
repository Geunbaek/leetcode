
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        p = [i for i in range(len(stones))]
        ans = len(stones)
        
        for i in range(1, len(stones)):
            for j in range(i):
                left = stones[j]
                right = stones[i]
                
                if left[0] == right[0] or left[1] == right[1]:
                    if find(i) != find(j):
                        union(i, j)
                        ans -= 1
        return len(stones) - ans
        
    