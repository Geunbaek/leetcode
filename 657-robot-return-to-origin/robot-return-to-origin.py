class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        movements = {
            "U": lambda x, y: (x, y - 1),
            "D": lambda x, y: (x, y + 1),
            "L": lambda x, y: (x - 1, y),
            "R": lambda x, y: (x + 1, y),
        }
        for move in moves:
            x, y = movements[move](x, y)
        return x == 0 and y == 0