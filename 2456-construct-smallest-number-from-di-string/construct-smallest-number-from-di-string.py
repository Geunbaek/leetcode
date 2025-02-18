class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        def recur(depth, prev):
            if depth >= n:
                answer.append(prev)
                return
            
            p = pattern[depth]

            for i in range(1, 10):
                if used[i] == 1:
                    continue
                
                if p == "I" and int(prev[-1]) > i:
                    continue
                if p == "D" and int(prev[-1]) < i:
                    continue

                used[i] = 1
                recur(depth + 1, prev + str(i))
                used[i] = 0
            
        n = len(pattern)
        used = [0 for _ in range(10)]
        answer = []

        for i in range(1, 10):
            used[i] = 1
            recur(0, str(i))
            used[i] = 0

        answer.sort()

        return answer[0]