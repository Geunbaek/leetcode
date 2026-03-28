class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = ['' for _ in range(n)]
        c = ord('a')
        for y in range(n):
            if not word[y]:
                if c > ord('z'):
                    return ""
                word[y] = chr(c)
                for x in range(y + 1, n):
                    if lcp[y][x]:
                        word[x] = chr(c)
                c += 1
        for y in range(n - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                if word[y] != word[x]:
                    if lcp[y][x]:
                        return ""
                else:
                    if y == n - 1 or x == n - 1:
                        if lcp[y][x] != 1:
                            return ""
                    else:
                        if lcp[y][x] != lcp[y + 1][x + 1] + 1:
                            return ""
        return "".join(word)
                    
