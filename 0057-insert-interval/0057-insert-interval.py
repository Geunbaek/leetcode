class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        stack = []
        
        def is_contain_range(i1, i2):
            s1, e1 = i1
            s2, e2 = i2
            
            if e1 < s2:
                return False
            return True
        
        for s, e in intervals:
            if stack and is_contain_range(stack[-1], (s, e)):
                s1, e1 = stack.pop()
                stack.append((min(s, s1), max(e, e1)))
            else:
                stack.append((s, e))
        return stack