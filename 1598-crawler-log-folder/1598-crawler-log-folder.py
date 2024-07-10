class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            oper = log[:-1]
            
            if oper == '..':
                if not stack:
                    continue
                stack.pop()
            
            elif oper == ".":
                continue
            
            else:
                stack.append(oper)
        return len(stack)
        