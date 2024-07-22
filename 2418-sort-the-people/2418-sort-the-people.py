class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ret = list(zip(names, heights))
        ret.sort(key = lambda x: -x[-1])
        return list(map(lambda x: x[0], ret))
        