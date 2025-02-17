class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def recur(depth, letter):
            if depth > n:
                return

            if letter:
                sub.add(letter)

            for char in tiles:
                index = ord(char) - ord("A")
                if alpha[index] == 0:
                    continue
                alpha[index] -= 1
                recur(depth + 1, letter + char)
                alpha[index] += 1

        n = len(tiles)
        alpha = [0 for _ in range(26)]
        sub = set()

        for char in tiles:
            index = ord(char) - ord("A")
            alpha[index] += 1

        recur(0, "")
        print(sub)
        return len(sub)
        