class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        n = len(counter)

        most_common = counter.most_common(n)

        print(most_common)

        even = float("inf")
        odd = float("-inf")
        for key, value in most_common:
            if value % 2 == 0:
                even = min(even, value)
            
            if value % 2 != 0:
                odd = max(odd, value)

        return odd - even