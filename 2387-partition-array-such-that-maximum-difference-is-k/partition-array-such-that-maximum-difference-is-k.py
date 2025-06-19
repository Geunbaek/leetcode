class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        answer = [[]]

        for num in nums:
            last = answer[-1]

            if not last:
                last.append(num)
                continue
            
            if num - last[0] <= k:
                last.append(num)
            else:
                answer.append([num])
        return len(answer)