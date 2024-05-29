class Solution:
    def numSteps(self, s: str) -> int:
        num = list(s)
        
        def add_num():
            nonlocal num
            n = len(num)
            flag = True
            for i in range(n - 1, -1, -1):
                if num[i] == "0":
                    num[i] = '1'
                    flag = False
                    break
                else:
                    num[i] = '0'
            if flag:
                num = ["1"] + num
        
        def div_num():
            num.pop()
            
        def is_one():
            return len(num) == 1 and num[0] == '1'
        
        def is_odd():
            n = len(num)
            return num[n - 1] == "1"
        
        answer = 0
        while not is_one():
            if is_odd():
                add_num()
            else:
                div_num()
            answer += 1
        return answer
            