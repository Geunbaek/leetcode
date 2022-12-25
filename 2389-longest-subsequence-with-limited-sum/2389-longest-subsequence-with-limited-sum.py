from itertools import combinations

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for q in queries:
            count = 0
            for num in nums:
                if q >= num:
                    q -= num
                    count += 1
                    
            answer.append(count)
        return answer
                