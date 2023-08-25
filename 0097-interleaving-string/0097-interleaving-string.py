class Solution:
    def isInterleave(self, s1, s2, s3):  
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        
        if l1 + l2 != l3:
            return False
        
        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True
        
        for y in range(l1 + 1):
            for x in range(l2 + 1):
                if y > 0 and s1[y - 1] == s3[x + y - 1]:
                    dp[y][x] |= dp[y - 1][x]
                if x > 0 and s2[x - 1] == s3[x + y - 1]:
                    dp[y][x] |= dp[y][x - 1]
        return dp[l1][l2]
