class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(lambda x: int(x), list(str(int("".join(map(str, num))) + k))))
        