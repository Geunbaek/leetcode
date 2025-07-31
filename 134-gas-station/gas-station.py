class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        n = len(gas)

        total = 0
        start = 0

        for i in range(n):
            total += gas[i]

            if total < cost[i]:
                start = i + 1
                total = 0
            else:
                total -= cost[i]


        return start