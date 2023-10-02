class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count = 0
        b_count = 0
        stack = []
        
        for color in colors:
            if not stack:
                stack.append(color)
                continue
            
            if stack[-1][-1] == color:
                stack[-1] += color
            else:
                stack.append(color)
            
        for el in stack:
            if len(el) >= 3:
                if el[0] == "A":
                    a_count += len(el) - 2
                else:
                    b_count += len(el) - 2
        return a_count > b_count
        