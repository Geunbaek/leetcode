class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cache = {chr(ord("a") + i): 0 for i in range(26)}
        stack = []
        seen = set()
        
        for char in s:
            cache[char] += 1
            
        for char in s:
            cache[char] -= 1
            
            if char in seen:
                 continue
                    
            while stack and char < stack[-1] and cache[stack[-1]] >= 1:
                seen.remove(stack.pop())
                
            seen.add(char)
            stack.append(char)
            
        return "".join(stack)
        