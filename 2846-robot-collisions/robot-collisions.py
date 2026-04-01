class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        status = []

        for i, (p, h, d) in enumerate(zip(positions, healths, directions)):
            status.append([i, p, h, d])
        status.sort(key = lambda x: x[1])

        stack = []

        for i, (j, p, h, d) in enumerate(status):
            while stack and d == 'L' and stack[-1][-1] == 'R' and status[i][2] > 0:
                last_health = status[stack[-1][0]][2]
                now_health = status[i][2]
                if last_health == now_health:
                    status[stack[-1][0]][2] = 0
                    status[i][2] = 0
                    stack.pop()
                    break
                elif last_health > now_health:
                    status[stack[-1][0]][2] -= 1
                    status[i][2] = 0
                    break
                else:
                    status[i][2] -= 1
                    status[stack[-1][0]][2] = 0
                    stack.pop()
            
            if status[i][2] > 0:
                stack.append((i, d))
        return list(map(lambda x: x[2], sorted(map(lambda x: status[x[0]], stack), key = lambda x: x[0])))