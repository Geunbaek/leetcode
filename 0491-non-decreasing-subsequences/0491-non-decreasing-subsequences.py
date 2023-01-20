from itertools import combinations

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return []
        answer=set()
        for i in range(2,len(nums)+1):
            for c in combinations(nums, i):
                if list(c)== sorted(c) and c not in answer:
                    answer.add(c)
        return sorted(answer)