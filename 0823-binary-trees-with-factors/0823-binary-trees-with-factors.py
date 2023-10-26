
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        def oper(num):  
            for n in arr:
                if n >= num:
                    return
                
                if num % n == 0 and num // n in cache:
                    print(n, num)
                    mod = num // n
                    dp[num] += (dp[n] * dp[mod])
                    dp[num] %= MOD
         
        MOD = 10**9 + 7
        n = len(arr)
        arr.sort()
        cache = set(arr)
        
        dp = {num: 1 for num in arr}
        
        for i in range(n):
            oper(arr[i])
     
        return sum(dp.values()) % MOD
                
        