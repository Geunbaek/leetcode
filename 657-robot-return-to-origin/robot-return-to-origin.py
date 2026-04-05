class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = Counter(moves)
        return m['D'] == m['U'] and m['L'] == m['R']