class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a=Counter(s)
        b=Counter(t)
        
        diff =0
        print(list(a.items()))
        for key,val in a.items():
            bc=b[key]
            diff += abs(val - bc)
        for key,val in b.items():
            if a[key]==0:
                diff += val
        return diff //2
        