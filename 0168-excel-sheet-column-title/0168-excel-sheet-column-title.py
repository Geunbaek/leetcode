class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = {
            i : chr(ord('A') + i) for i in range(26)
        }
        answer = []
        
        while columnNumber > 0:
            columnNumber -= 1
            answer.append(alpha[columnNumber % 26])
            columnNumber //= 26
    

        return "".join(answer[::-1])