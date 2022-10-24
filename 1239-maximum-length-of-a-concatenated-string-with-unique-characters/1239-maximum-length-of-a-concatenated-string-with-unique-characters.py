class Solution:
    def maxLength(self, arr: List[str]) -> int:
        answer = 0
        def recur(now, depth):
            nonlocal answer
            flag = False
            
            for i in range(depth + 1, len(arr)):
                if len(set(arr[i])) != len(arr[i]):
                    continue
                if len(now | set(arr[i])) == len(now) + len(arr[i]):
                    recur(now | set(arr[i]), i)
                    flag = True
                    
            if not flag:
                answer = max(answer, len(now))
                    
        for i in range(len(arr)):
            if len(set(arr[i])) != len(arr[i]):
                continue
            recur(set(arr[i]), i)

        return answer

                    
        