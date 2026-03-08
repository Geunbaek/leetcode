class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        num_set = set()

        for num in nums:
            num_set.add(int(num, 2))
        for i in range(0, 2**n):
            if i not in num_set:
                return bin(i)[2:].zfill(n)
        return ""