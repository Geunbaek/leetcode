class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = []
        temp = ""
        for digit in num:
            if not temp:
                temp += digit
                continue
                
            if temp[-1] == digit:
                temp += digit
            else:
                temp = digit
            
            if len(temp) == 3:
                answer.append(int(temp))
        if not answer:
            return ""
        answer.sort()
        return str(answer.pop()).zfill(3)
        