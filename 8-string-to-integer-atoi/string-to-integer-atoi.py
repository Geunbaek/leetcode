def skip_whitespace(s):
    n = len(s)
    for i in range(n):
        if s[i] != " ":
            return i
    return n

def get_sign(i, s):
    n = len(s)
    for j in range(i, n):
        if s[j] == '+':
            return 1, j + 1
        elif s[j] == '-':
            return -1, j + 1
        break
    return 1, i

def get_num(i, s):
    n = len(s)
    num = ''
    for j in range(i, n):
        if s[j].isdigit():
            num += s[j]
        else:
            break
    return int(num) if num else 0

MIN = -2147483648
MAX = 2147483647

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = skip_whitespace(s)
        sign, i = get_sign(i, s)
        num = get_num(i, s)
        result = sign * num
        if result > MAX:
            return MAX
        elif result < MIN:
            return MIN
        return result
