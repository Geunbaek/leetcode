class Solution:
    def minMaxDifference(self, num: int) -> int:
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
            new_min_num = change_num(num, str(i), '0')
            _max = max(_max, new_max_num)
            _min = min(_min, new_min_num)
        print(_max, _min)
        return _max - _min