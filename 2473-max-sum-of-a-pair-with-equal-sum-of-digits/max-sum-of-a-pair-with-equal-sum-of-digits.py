class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        자리수_합_캐시 = defaultdict(list)


        for 수 in nums:
            자리수_합 = sum(map(lambda x: int(x), str(수)))
            자리수_합_캐시[자리수_합].append(수)

        정답 = -1
        for 자리수_합, 수_집합 in 자리수_합_캐시.items():
            정렬된_수_집합 = sorted(list(수_집합))
            
            if len(정렬된_수_집합) < 2:
                continue
            
            정답 = max(정답, 정렬된_수_집합.pop() + 정렬된_수_집합.pop())

        return 정답
        
