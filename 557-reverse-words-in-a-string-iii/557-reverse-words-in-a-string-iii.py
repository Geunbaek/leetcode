class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        for el in s.split():
            ret.append(el[::-1])
        return " ".join(ret)
        