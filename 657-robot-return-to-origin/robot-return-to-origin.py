class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = defaultdict(int)

        for move in moves:
            m[move] += 1

        return m['D'] == m['U'] and m['L'] == m['R']