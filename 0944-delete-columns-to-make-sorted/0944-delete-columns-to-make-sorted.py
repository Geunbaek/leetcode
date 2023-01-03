class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer=0
        for x in range(len(strs[0])):
            for y in range(1,len(strs)):
                if ord(strs[y][x]) < ord(strs[y-1][x]):
                    answer+=1
                    break

                
        return answer
            
        