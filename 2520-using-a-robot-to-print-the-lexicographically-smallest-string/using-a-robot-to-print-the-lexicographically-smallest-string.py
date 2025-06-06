class Solution:
    def robotWithString(self, s: str) -> str:
        def get_min_char():
            return min(counter.keys())
        
        def minus_char(char):
            counter[char] -= 1
            if counter[char] == 0:
                del counter[char]
        
        counter = Counter(s)
        q = deque(s)
        stack = []
        answer = []

        while counter:
            c = get_min_char()
            while q:
                first = q.popleft()
                if not stack:
                    stack.append(first)
                    minus_char(first)
                    continue

                if stack[-1] > c:
                    stack.append(first)
                    minus_char(first)
                else:
                    q.appendleft(first)
                    break
            if counter:
                c = get_min_char()
                while stack and c >= stack[-1]:
                    answer.append(stack.pop())

        while stack:
            answer.append(stack.pop())

        return "".join(answer)