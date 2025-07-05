class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1

        for key, cnt in Counter(arr).items():
            if key == cnt and answer < key:
                answer = cnt
        return answer