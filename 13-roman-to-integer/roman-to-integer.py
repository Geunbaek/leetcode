class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        def calc_roman_num(roman_num):
            stack = []
            for char in roman_num:
                if stack and stack[-1][-1] == char:
                    stack[-1] += char
                else:
                    stack.append(char)
            ret = 0
            for i, s in enumerate(stack):
                if i == 0:
                    for char in s:
                        ret += roman[char]
                else:
                    ret = roman[s] - ret

            return ret


        num = 0
        stack = []
        
        for char in s:
            if stack and roman[stack[-1][-1]] <= roman[char]:
                stack[-1] += char
            else:
                stack.append(char)

        for char in stack:
            print(calc_roman_num(char), char)
            num += calc_roman_num(char)

        return num
            

        