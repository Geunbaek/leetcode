from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        return "".join(sorted(list(s),key=lambda x:(-c[x],x)))
        