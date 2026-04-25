class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count("L")
        r = moves.count("R")

        _ = len(moves) - l - r

        return abs(l - r) + _