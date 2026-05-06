class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        r, c = len(boxGrid), len(boxGrid[0])
        ret = []

        for x in range(c):
            ret.append([])
            for y in range(r - 1, -1, -1):
                ret[-1].append(boxGrid[y][x])
        nr, nc = len(ret), len(ret[0])
        for y in range(nr - 1, -1, -1):
            for x in range(nc):
                print(y, x)
                if ret[y][x] == '.':
                    for k in range(y - 1, -1, -1):
                        if ret[k][x] == '*':
                            break
                        if ret[k][x] == '#':
                            ret[y][x], ret[k][x] = ret[k][x], ret[y][x]
                            break
        return ret