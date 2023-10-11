class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []
        
        for s, e in flowers:
            starts.append(s)
            ends.append(e + 1)
            
        starts.sort()
        ends.sort()
        
        ans = []
        
        for p in people:
            s = bisect_right(starts, p)
            e = bisect_right(ends, p)
            ans.append(s - e)
            
        return ans
        