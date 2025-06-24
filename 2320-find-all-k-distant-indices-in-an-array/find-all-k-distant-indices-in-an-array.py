class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = []
        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                keys.append(i)

        answer = []
        for i in range(n):
            flag = False

            for key in keys:
                if abs(key - i) <= k:
                    flag = True

                if flag:
                    break

            if flag:
                answer.append(i)

        return answer
        