import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1, 1001)]
        heapq.heapify(self.h)
        self.cache = set([i for i in range(1, 1001)])
        

    def popSmallest(self) -> int:
        if not self.h:
            return
        smallest = heapq.heappop(self.h)
        self.cache.remove(smallest)
        return smallest
        

    def addBack(self, num: int) -> None:
        if num in self.cache:
            return
        self.cache.add(num)
        heapq.heappush(self.h, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)