class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def get_count(num):
            ret = 0
            for i in range(1, num + 1):
                ret += i
            return ret
                
        zeros = []
        count = answer = 0
        
        for num in nums:
            if num == 0:
                count += 1
            else:
                if count:
                    zeros.append(count)
                count = 0
        if count:
            zeros.append(count)
      
        for zero in zeros:
            answer += get_count(zero)
        return answer
            
        