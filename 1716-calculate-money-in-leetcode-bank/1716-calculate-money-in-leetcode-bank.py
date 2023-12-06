class Solution:
    def totalMoney(self, n: int) -> int:
        ans =0 
        
        for i in range(n):
            a = (i // 7) + 1
            b = (i % 7)
            
            ans += a + b
            
        return ans
        