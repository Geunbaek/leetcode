from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if max(people) > limit:
            return 0
        people.sort()
        people = deque(people)
        ans = 0
        while people:
            temp = 0
            cnt = 0
            while people and temp + people[-1] <= limit and cnt < 2:
                temp += people.pop()
                cnt += 1
    
            while people and temp + people[0] <= limit and cnt < 2:
                temp += people.popleft()
                cnt += 1
            ans += 1
        return ans