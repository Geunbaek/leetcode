import heapq
class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        if not self.max or not self.min:
            heapq.heappush(self.max, -num)
        else:
            if num >= -self.max[0]:
                heapq.heappush(self.min, num)
            else:
                heapq.heappush(self.max, -num)
                
        while not (len(self.max) == len(self.min) or len(self.max) == len(self.min) + 1):
            if len(self.max) > len(self.min):
                heapq.heappush(self.min, -heapq.heappop(self.max))
            else:
                heapq.heappush(self.max, -heapq.heappop(self.min))
        self.size += 1
                
    def findMedian(self) -> float:
        if self.size == 0:
            return None
        if self.size % 2 != 0:
            return -self.max[0]
        else:
            return (-self.max[0] + self.min[0]) / 2
    
            
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()