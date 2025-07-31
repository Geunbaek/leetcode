class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            now = set([x])
            for y in cur:
                now.add(x | y)
            cur = now
            ans |= cur
        return len(ans)