class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m:
            return False
        double_s = s + s
        for i in range(n):
            if double_s[i: i + n] == goal:
                return True
        return False