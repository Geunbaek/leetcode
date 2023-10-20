# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = self.flat(nestedList)
        self.index = 0
        self.size = len(self.arr)
        
    def flat(self, arr):
        ret = []
        for el in arr:
            if len(el._list) >= 1:
                ret.extend(self.flat(el._list))
            else:
                if el._integer is not None:
                    ret.append(el._integer)
        return ret
        
    def next(self) -> int:
        ret = self.arr[self.index]
        self.index += 1
        return ret
        
    def hasNext(self) -> bool:
        return self.size > self.index
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())