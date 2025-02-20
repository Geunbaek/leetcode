class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        
        s = set()
        for num in nums:
            s.add(int(num, 2))
        
        for i in range(2 ** 16):
            if i not in s:
                return bin(i)[2:].zfill(l)

        return ""