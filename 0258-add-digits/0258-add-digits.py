class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = 0
            for char in str(num):
                temp += int(char)
            num = temp
        return num
                
        