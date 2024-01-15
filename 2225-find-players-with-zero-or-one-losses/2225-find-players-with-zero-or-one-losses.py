from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = defaultdict(int)
        participants = set()
        for winner, loser in matches:
            result[loser] += 1
            participants.add(loser)
            participants.add(winner)
        
        answer = [[], []]
        for player in participants:
            if result[player] == 0:
                answer[0].append(player)
            elif result[player] == 1:
                answer[1].append(player)
        for el in answer:
            el.sort()
        return answer
            