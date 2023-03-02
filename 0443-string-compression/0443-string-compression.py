class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = []
        
        for char in chars:
            if not stack:
                stack.append([char, 1])
                continue
                
            if stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
                
        answer = []
        for char, cnt in stack:
            answer.append(char)
            if cnt > 1:
                answer.extend(list(str(cnt)))
                
                
        for i in range(len(answer)):
            chars[i] = answer[i]
            
        return len(answer)