from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        self.nums = set()
        

    def addNum(self, value: int) -> None:
        self.nums.add(value)
        
    def getIntervals(self) -> List[List[int]]:
        seenNums = set()
        intervals = []
        
        for num in self.nums:
            if num in seenNums:
                continue
            
            left = right = num
            seenNums.add(num)
            
            while left - 1 in self.nums:
                left -= 1
                seenNums.add(left)
            
            while right + 1 in self.nums:
                right += 1
                seenNums.add(right)
            intervals.append([left, right])
            
        return sorted(intervals)
       
            


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()