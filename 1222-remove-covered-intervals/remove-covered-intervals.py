class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        stack = []
        for a, b in intervals:
            if not stack:
                stack.append((a, b))
                continue

            c, d = stack[-1]

            if (c <= a and b <= d):
                continue
            else:
                stack.append((a, b))
        return len(stack)