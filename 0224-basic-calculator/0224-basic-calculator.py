import re

def operate(value, result, oper):
    if not oper:
        value = result
    else:
        if oper == "+":
            value += result
        else:
            value -= result
    return value

class Solution:
    def calculate(self, s: str) -> int:
        def dfs(depth):
            value = 0
            oper = ""
            while True:
                if depth >= len(s):
                    return value, depth + 1
                
                char = s[depth]
                if char == " " or not char:
                    depth += 1
                    continue
                
                if char == "(":
                    result, lastDepth = dfs(depth + 1)
                    value = operate(value, result, oper)
                    depth = lastDepth
                    continue
                
                if char == ")":
                    return value, depth + 1
        
                if char.isdigit():
                    value = operate(value, int(char), oper)
                else:
                    oper = char
                    
                depth += 1
        s = re.split(r"([()\+\- ])", s)
        print(s)
        return dfs(0)[0]