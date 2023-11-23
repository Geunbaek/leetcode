class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer =[]
        for li, ri in zip(l, r):
            sub_nums = sorted(nums[li: ri + 1])
            diff = sub_nums[1] - sub_nums[0]
            for i in range(2, len(sub_nums)):
                if sub_nums[i] - sub_nums[i - 1] != diff:
                    answer.append(False)
                    break
            else:
                answer.append(True)
                
        return answer
            
        