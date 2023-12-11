class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = n / 4
        
        counter = Counter(arr)
        return counter.most_common(1)[0][0]
        