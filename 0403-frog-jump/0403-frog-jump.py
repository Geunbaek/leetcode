class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1: return False 				
        
        indices = {v:i for i,v in enumerate(stones)}	
        
        @cache
        def dfs(i,lastStep):
            if i==len(stones)-1: 						
                return True
            res = False
            for curStep in range(lastStep-1,lastStep+2):	
                if stones[i]+curStep in indices and indices[stones[i]+curStep]>i:
                    res = res or dfs(indices[stones[i]+curStep],curStep)
            return res
        
        return dfs(1,1)