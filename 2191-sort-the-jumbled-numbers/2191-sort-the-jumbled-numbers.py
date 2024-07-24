class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def format(x):
            ret = ""
            str_x = str(x)
            for c in str_x:
                ret += str(mapping[int(c)])
            return int(ret)
        
        nums.sort(key = lambda x: format(x))
        return nums