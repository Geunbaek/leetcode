class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_sub(word, sub, p):
            stack = []
            point = 0

            for char in word:
                if stack and stack[-1] == sub[0] and char == sub[1]:
                    stack.pop()
                    point += p
                    continue
                stack.append(char)
            return "".join(stack), point

        answer = 0
        sub = [(x, "ab"), (y, "ba")]
        sub.sort(reverse=True)

        for p, sub_s in sub:
            s, point = remove_sub(s, sub_s, p)
            answer += point
        
        return answer

        