from collections import deque

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        q = deque(s)
        word_board = [[] for _ in range(numRows)]
        
        is_upper = False
        i = 0
        while q:
            char = q.popleft()
            word_board[i].append(char)
            
            if i == 0 or i == numRows - 1:
                is_upper = not is_upper
            
            if is_upper:
                i += 1
            else:
                i -= 1
        
        answer = ""
        for l in word_board:
            answer += "".join(l)
            
        return answer
                

        
        
        