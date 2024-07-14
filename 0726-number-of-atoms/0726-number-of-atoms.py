class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        
        stack = [defaultdict(int)]
        
        i = 0
    
        while i < n:
            if formula[i] == "(":
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ")":
                temp = stack.pop()
                mul = ""
                i += 1
                while i < n and formula[i].isdigit():
                    mul += formula[i]
                    i += 1
                
                if mul:
                    for k in temp.keys():
                        temp[k] *= int(mul)
                for k in temp.keys():
                    stack[-1][k] += temp[k]
            else:
                temp = formula[i]
                i += 1
                
                while i < n and formula[i].islower():
                    temp += formula[i]
                    i += 1
                
                count = ""
                while i < n and formula[i].isdigit():
                    count += formula[i]
                    i += 1
                
                if not count:
                    stack[-1][temp] += 1
                else: 
                    stack[-1][temp] += int(count)
                    
        cache = dict(sorted(stack[0].items()))
        
        answer = ""
        for k in cache.keys():
            answer += k
            if cache[k] > 1:
                answer += str(cache[k])
                    
        print(stack)
        print(cache)
        return answer
                
            