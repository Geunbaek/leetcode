class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        l_stack = []
        
        robots = []
        
        for i, (p, h, d) in enumerate(zip(positions, healths, directions)):
            robots.append((p, h, d, i))
        robots.sort()
        
        for p, h, d, i in robots:
            if d == "R":
                stack.append((p, h, d, i))
            else:
                if not stack:
                    l_stack.append((p, h, d, i))
                    continue
                
                while stack:
                    p1, h1, d1, i1 = stack.pop()
                    if h1 < h:
                        h -= 1
                    elif h1 > h:
                        h = 0
                        stack.append((p1, h1 - 1, d1, i1))
                        break
                    else:
                        h = 0
                        break

                if not stack and h:
                    l_stack.append((p, h, d, i))
        stack.extend(l_stack)
        stack.sort(key = lambda x: x[-1])
        answer = list(map(lambda x: x[1], stack))
        return answer
        