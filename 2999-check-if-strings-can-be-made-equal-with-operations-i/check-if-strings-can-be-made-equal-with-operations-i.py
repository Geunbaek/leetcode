class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        odd_set1 = defaultdict(int)
        even_set1 = defaultdict(int)
        odd_set2 = defaultdict(int)
        even_set2 = defaultdict(int)
        for i, c in enumerate(s1):
            if i % 2 == 0:
                odd_set1[c] += 1
            else:
                even_set1[c] += 1
        for i, c in enumerate(s2):
            if i % 2 == 0:
                odd_set2[c] += 1
            else:
                even_set2[c] += 1
        
        return odd_set1 == odd_set2 and even_set1 == even_set2