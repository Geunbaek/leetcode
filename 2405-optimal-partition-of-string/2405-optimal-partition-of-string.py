class Solution:
    def partitionString(self, s: str) -> int:
        temp=""
        ans=0
        for char in s:
            if char in temp:
                temp=""
                ans+=1
            temp+=char
        if temp:
            ans+=1
        return ans
    