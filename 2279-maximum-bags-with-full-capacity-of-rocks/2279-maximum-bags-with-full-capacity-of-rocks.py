class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = 0
        for c, r in sorted(zip(capacity, rocks), key = lambda x: (x[0] - x[1])):
            if additionalRocks >= c - r:
                additionalRocks -= c - r
                count += 1
            else:
                return count

        return count
        
            
      