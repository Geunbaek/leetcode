class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half=n
        n1=nums[:half]
        n2=nums[half:]
        ans = []
        for x,y in zip(n1,n2):
            ans.extend([x,y])
        return ans
        