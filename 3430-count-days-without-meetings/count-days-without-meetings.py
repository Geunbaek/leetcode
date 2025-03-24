class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        stack = []

        for start, end in meetings:
            if not stack:
                stack.append((start, end))
                continue

            last_start, last_end = stack.pop()
            if last_start <= start <= last_end:
                stack.append((last_start, max(last_end, end)))
            else:
                stack.append((last_start, last_end))
                stack.append((start, end))
        for s, e in stack:
            days -= (e - s) + 1
        return days