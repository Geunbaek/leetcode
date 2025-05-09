# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for x in range(n):
            for y in range(n):
                if x == y:
                    continue
                if knows(x, y) or not knows(y, x):
                    break
            else:
                return x
        return -1
            