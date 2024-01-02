class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        
        for num in nums:
            for i in range(len(ret)):
                if num in ret[i]:
                    continue
                ret[i].append(num)
                break
            else:
                ret.append([])
                ret[-1].append(num)
        
        return ret