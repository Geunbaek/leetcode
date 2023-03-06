class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cache = set(arr)
        for i in range(1, 2001):
            if i not in cache:
                k -= 1
            if k == 0:
                return i
        
        