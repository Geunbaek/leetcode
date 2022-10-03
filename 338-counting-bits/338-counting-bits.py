class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0, 1]
        temp = [1]
        while len(dp) < n + 1:
            temp2 = temp[:]
            for i in temp:
                temp2.append(i + 1)
            temp = temp2[:]
            dp.extend(temp2)
        return dp[:n + 1]
                             
                
            