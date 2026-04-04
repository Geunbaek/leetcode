class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        
        table = [["" for _ in range(cols)] for _ in range(rows)]

        for i, c in enumerate(encodedText):
            y = i // cols
            x = i % cols
            table[y][x] = c

        answer = ""

        x = 0
        nx, ny = 0, 0
        while nx < cols:
            answer += table[ny][nx]
            ny += 1
            nx += 1
            if ny >= rows:
                ny = 0
                nx = x + 1
                x = nx
        return answer.rstrip()