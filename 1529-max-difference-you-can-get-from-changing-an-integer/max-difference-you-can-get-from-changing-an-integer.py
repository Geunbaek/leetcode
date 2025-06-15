class Solution:
    def maxDiff(self, num: int) -> int:
        def change_num(num, target, new):
            str_num = list(str(num))

            for i in range(len(str_num)):
                if str_num[i] == target:
                    str_num[i] = new

            return int("".join(str_num))
        
        _min = float('inf')
        _max = float('-inf')

        for i in range(10):
            new_max_num = change_num(num, str(i), '9')
            new_min_num1 = change_num(num, str(i), '1')
            new_min_num2 = change_num(num, str(i), '0')
            if len(str(new_min_num1)) != len(str(new_min_num2)) or new_min_num2 == 0:
                _min = min(_min, new_min_num1)
            else:
                _min = min(_min, new_min_num2)
                
            _max = max(_max, new_max_num)
        return _max - _min