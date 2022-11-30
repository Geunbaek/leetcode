from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        countSet = set()
        
        for key, val in counter.items():
            if val in countSet:
                return False
            countSet.add(val)
        return True