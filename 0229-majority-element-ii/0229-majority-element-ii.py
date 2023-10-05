class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) / 3
        answer = []
        
        for num, cnt in Counter(nums).items():
            if cnt > times:
                answer.append(num)

        return answer