class Solution:
    def minimumDistance(self, word: str) -> int:
        dist=lambda a,b: (abs(a//6-b//6)+abs(a%6-b%6)) if a!=-1 else 0
        arr=[ord(char)-ord('A') for char in word]
        @lru_cache(None)
        def dfs(f1,f2,index):
            if index==len(word):
                return 0
            return min(
                dfs(f1, 
                    arr[index], index+1) + dist(f2, arr[index]), 
                    dfs(arr[index], f2, index+1) + 
                    dist(f1, arr[index])
                )
        
        return dfs(-1,-1,0)