import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = list(filter(lambda x: x, path.split("/")))
        stack = []
        
        for p in paths:
            if p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(p)
        return "/" + "/".join(stack)
            
        
        